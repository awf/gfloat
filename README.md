# gfloat: Generic floating-point types in Python

An implementation of generic floating point encode/decode logic,
handling various current and proposed floating point types:

 - IEEE binary16, binary32
 - OCP Float8: E5M2, E4M3
 - IEEE WG P3109: P{p} for p in 1..7

See (https://gfloat.readthedocs.io) for documentation.

## TODO:

All NaNs are the same, with no distinction between signalling or quiet, 
or between differently encoded NaNs.

