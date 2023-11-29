# gfloat: Generic floating-point types in Python

An implementation of generic floating point encode/decode logic,
handling various current and proposed floating point types:

 - IEEE binary16, binary32
 - OCP Float8: E5M2, E4M3
 - IEEE WG P3109: P{p} for p in 1..7

All types are decoded using a consistent set of parameters, defined in the
class `FormatInfo`:
```py
  k: int                # number of bits in the format
  precision: int        # number of significand bits (including implicit leading bit)
  emax: int             # Largest exponent, emax = floor(log_2(maxFinite)) 
  has_infs : bool       # Set if format encodes +/- Infinity.
                        # If set, the highest [lowest] non-nan value is replaced by +Inf [-Inf]
  num_high_nans: bool   # Number of NaNs are encoded in the highest encoding slots (+/-)
  has_nz: bool          # Set if format encodes -0 at sgn=1,exp=0,significand=0
                        # if not, that encoding decodes to a NaN labelled NaN_0
```

## TODO:

All NaNs are the same, with no distinction between signalling or quiet, 
or between differently encoded NaNs.

