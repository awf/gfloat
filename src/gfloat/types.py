from dataclasses import dataclass
from enum import Enum
import numpy as np

@dataclass
class FormatInfo:
    """
    Class describing a floating-point format, parametrized
    by width, precision, and special value encoding rules.

    """

    #: Short name for the format, e.g. binary32, bfloat16
    name: str

    #: Number of bits in the format
    k: int

    #: Number of significand bits (including implicit leading bit)
    precision: int

    #: Largest exponent, emax, which shall equal floor(log_2(maxFinite))
    emax: int

    #: Set if format encodes -0 at (sgn=1,exp=0,significand=0).
    #: If False, that encoding decodes to a NaN labelled NaN_0
    has_nz: bool

    #: Set if format includes +/- Infinity.
    #: If set, the non-nan value with the highest encoding for each sign (s)
    #: is replaced by (s)Inf.
    has_infs: bool

    #: Number of NaNs that are encoded in the highest encodings for each sign
    num_high_nans: int

    #: ## Derived values

    @property
    def tSignificandBits(self):
        """The number of trailing significand bits, t"""
        return self.precision - 1

    @property
    def expBits(self):
        """The number of exponent bits, w"""
        return self.k - self.precision


class FloatClass(Enum):
    """
    Enum for the classification of a FloatValue.
    """

    NORMAL = 1  #: A positive or negative normalized non-zero value
    SUBNORMAL = 2  #: A positive or negative subnormal value
    ZERO = 3  #: A positive or negative zero value
    INFINITE = 4  # A: positive or negative infinity (+/-Inf)
    NAN = 5  #: Not a Number (NaN)

@dataclass
class FloatValue:
    """
    A floating-point value decoded in great detail.
    """

    ival: int  #: Integer code point
    
    
    #: Value. Assumed to be exactly round-trippable to python float.
    #: This is true for all <64bit formats known in 2023.
    fval: float
    
    valstr: str  #: Value as string, assuming all code points finite
    exp: int  #: Raw exponent without bias
    expval: int  #: Exponent, bias subtracted
    significand: int  #: Significand as an integer
    fsignificand: float  #: Significand as a float in the range [0,2)
    signbit: int  #: Sign bit: 1 => negative, 0 => positive
    fclass: FloatClass  #: See FloatClass
    fi: FormatInfo  # Backlink to FormatInfo

    @property
    def signstr(self):
        """Return "+" or "-" according to signbit"""
        return "+" if self.signbit else "-"
