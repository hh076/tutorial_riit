import sys, os
from ctypes import *

#liblapack = CDLL( "/Volumes/Home/honda/local/lib/liblapack.dylib" )  # My BLAS/Lapack
liblapack = CDLL( "/usr/lib64/liblapack.so" )  #System BLAS/Lapack

TYPE_PTR_VOID   = c_void_p
TYPE_PTR_CHAR   = POINTER( c_char   )
TYPE_PTR_INT    = POINTER( c_int32  )
TYPE_PTR_DOUBLE = POINTER( c_double )

### array ###
liblapack.dspgv_.restype  = TYPE_PTR_VOID
#        soubroutine dspgv_(  itype,        jobz,          uplo,          n,            ap,              bp,
liblapack.dspgv_.argtypes = [ TYPE_PTR_INT, TYPE_PTR_CHAR, TYPE_PTR_CHAR, TYPE_PTR_INT, TYPE_PTR_DOUBLE, TYPE_PTR_DOUBLE,
#                             w,               z,               ldz,          work,            info )
                              TYPE_PTR_DOUBLE, TYPE_PTR_DOUBLE, TYPE_PTR_INT, TYPE_PTR_DOUBLE, TYPE_PTR_INT ]
