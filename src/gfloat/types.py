from dataclasses import dataclass
from enum import Enum


@dataclass
class FormatInfo:
    name: str
    k: int  # number of bits in the format
    precision: int  # number of significand bits (including implicit leading bit)
    emax: int  # Largest exponent, emax = floor(log_2(maxFinite))
    has_nz: bool  # Set if format encodes -0 at sgn=1,exp=0,significand=0
    # if not, that encoding decodes to a NaN labelled NaN_0
    has_infs: bool  # Set if format encodes +/- Infinity.
    # If set, the highest [lowest] non-nan value is replaced by +Inf [-Inf]
    num_high_nans: bool  # Number of NaNs are encoded in the highest encoding slots (+/-)

    @property
    def significandBits(self):
        return self.precision - 1

    @property
    def expBits(self):
        return self.k - self.precision

    # e.g. for binary8{p=3,Z0,I1,H3}:
    #     0_11111_00 = Inf
    #     0_11111_01 = NaN_{+1}
    #     0_11111_10 = NaN_{+2}
    #     0_11111_11 = NaN_{+3}
    #     1_11111_00 = -Inf
    #     1_11111_01 = NaN_{-1}
    #     1_11111_10 = NaN_{-2}
    #     1_11111_11 = NaN_{-3}
    # e.g. for binary8{p=3,emax=32,Z1,I0,H1}:
    #     0_11111_10 = 448.0
    #     0_11111_11 = NaN_{+1}
    #     1_11111_10 = -448.0
    #     1_11111_11 = NaN_{-3}


class FloatClass(Enum):
    NORMAL = 1  # A positive or negative normalized non-zero value
    SUBNORMAL = 2  # A positive or negative subnormal value
    ZERO = 3  # A positive or negative subnormal zero value
    INFINITE = 4  # A positive or negative infinity
    NAN = 5  # A NaN


@dataclass
class FloatValue:
    """
    A floating-point value in detail
    """

    ival: int  # Integer code point
    fval: float  # Value [Note 1]
    valstr: str  # Value as string, assuming all code points finite
    exp: int  # Raw exponent without bias
    expval: int  # Exponent, bias subtracted
    significand: int  # Significand as an integer
    fsignificand: float  # Significand as a float in the range [0,2)
    signbit: int  # Sign bit: 1 => negative, 0 => positive
    signstr: str  # String representation of sign
    fclass: FloatClass  # See FloatClass
    fi: FormatInfo  # Backlink to FormatInfo

    # [Note 1]
    # Values are assumed to be exactly round-trippable to python float == float64.
    # This is true for all <64bit formats known in 2023.
