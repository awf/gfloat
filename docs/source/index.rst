.. GFloat documentation master file, created by
   sphinx-quickstart on Tue Nov 28 20:33:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

GFloat: Generic floating point formats in Python
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

GFloat is designed to allow experimentation with a variety of floating-point
formats in Python.  Formats are parameterized by the primary IEEE-754 parameters
of:

  * Width in bits (k)
  * Precision (p)
  * Maximum exponent (emax)

with additional fields defining the encoding of infinities, Not-a-number (NaN) values, 
and negative zero. 

API
===

.. autoclass:: gfloat.FormatInfo()
   :members:
.. autoclass:: gfloat.FloatClass()
   :members:
.. autoclass:: gfloat.FloatValue()
   :members:
.. autofunction:: gfloat.decode_float


Index and Search
================

* :ref:`genindex`
* :ref:`search`
