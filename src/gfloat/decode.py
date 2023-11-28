from .types import FormatInfo, FloatValue, FloatClass

import numpy as np


def decode_float(i: int, fi: FormatInfo) -> FloatValue:
    k = fi.k
    p = fi.precision
    t = p - 1  # trailing significand field width
    w = k - p

    signmask = 1 << (k - 1)
    signbit = 1 if i & signmask else 0
    sign = -1 if signbit else 1

    exp = (i & (signmask - 1)) >> t
    significand = i & ((1 << t) - 1)

    # Calculate whether all of the all-bits-one-exponent values contain specials.
    # If so, emax will be obtained for exponent value 2^w-2, otherwise it is 2^w-1
    num_posinfs = 1 if fi.has_infs else 0
    all_bits_one_full = (fi.num_high_nans + num_posinfs == 2 ** (p - 1)) or (
        fi.has_infs and w == 0
    )

    # Compute exponent bias.
    exp_for_emax = 2**w - (2 if all_bits_one_full else 1)
    expBias = exp_for_emax - fi.emax

    isnormal = exp != 0
    if isnormal:
        expval = exp - expBias
        fsignificand = 1.0 + significand * 2**-t
    else:
        expval = 1 - expBias
        fsignificand = significand * 2**-t

    # val: the raw value excluding specials
    val = sign * fsignificand * 2**expval

    # valstr: string representation of value in base 10
    # If the representation does not roundtrip to the value,
    # it is preceded by a "~" to indicate "approximately equal to"
    signstr = "-" if sign == -1 else "+"
    valstr = f"{val}"
    if len(valstr) > 14:
        valstr = f"{val:.8}"
    if float(valstr) != val:
        valstr = "~" + valstr

    # Now overwrite the raw value with specials: Infs, NaN, -0, NaN_0
    signed_infinity = -np.inf if signbit else np.inf

    fval = val
    # All-bits-one exponent (ABOE)
    if exp == 2**w - 1:
        min_i_with_nan = 2 ** (p - 1) - fi.num_high_nans
        if significand >= min_i_with_nan:
            fval = np.nan
        if fi.has_infs and significand == min_i_with_nan - 1:
            fval = signed_infinity

    # Negative zero or NaN
    if i == signmask:
        if fi.has_nz:
            fval = -0.0
        else:
            fval = np.nan

    # Compute FloatClass
    fclass = None
    if fval == 0:
        fclass = FloatClass.ZERO
    elif np.isnan(fval):
        fclass = FloatClass.NAN
    elif np.isfinite(fval):
        if isnormal:
            fclass = FloatClass.NORMAL
        else:
            fclass = FloatClass.SUBNORMAL
    else:
        fclass = FloatClass.INFINITE

    # update valstr if a special value
    if fclass not in (FloatClass.ZERO, FloatClass.SUBNORMAL, FloatClass.NORMAL):
        valstr = str(fval)

    return FloatValue(
        i,
        fval,
        valstr,
        exp,
        expval,
        significand,
        fsignificand,
        signbit,
        signstr,
        fclass,
        fi,
    )
