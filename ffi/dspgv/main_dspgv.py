import sys, numpy
import wrap_dspgv
from ctypes import *

#############################################
#############################################
#############################################
def conv_char_to_ptr( c ):
    ptr = numpy.array( [ c ], dtype = numpy.int8 ).ctypes.data_as( POINTER( c_int8 ) )
    return ptr

def conv_int_to_ptr_int32( n ):
    ptr = numpy.array( [ n ], dtype = numpy.int32 ).ctypes.data_as( POINTER( c_int32 ) )
    return ptr

def conv_numpy_int32_to_ptr( array ):
    return array.ctypes.data_as( POINTER( c_int32 ) )

def conv_numpy_double_to_ptr( array ):
    return array.ctypes.data_as( POINTER( c_double ) )

#############################################
#############################################
#############################################

line = sys.stdin.readline()
str  = line[:-1].split()
ndim = int( str[ 0 ] )
nsize = ( ndim * ( ndim + 1 ) ) // 2

itype = numpy.array( [ 1 ], dtype = numpy.int32 )
jobz  = 'V'
uplo  = 'U'
n     = numpy.array( [ ndim  ],       dtype = numpy.int32 )
ap    = numpy.empty( [ nsize ],       dtype = numpy.float64 )
bp    = numpy.empty( [ nsize ],       dtype = numpy.float64 )
w     = numpy.empty( [ ndim  ],       dtype = numpy.float64 )
z     = numpy.empty( [ ndim * ndim ], dtype = numpy.float64 )
ldz   = numpy.array( [ ndim ],        dtype = numpy.int32 )
wk    = numpy.empty( [ ndim * 3 ],    dtype = numpy.float64 )
info  = numpy.empty( [ 1 ],           dtype = numpy.int32 )

ptr_itype = conv_numpy_int32_to_ptr( itype )
ptr_jobz  = c_char_p( b'V' )
ptr_uplo  = c_char_p( b'U' )
ptr_n     = conv_numpy_int32_to_ptr( n )
ptr_ap    = conv_numpy_double_to_ptr( ap )
ptr_bp    = conv_numpy_double_to_ptr( bp )
ptr_w     = conv_numpy_double_to_ptr( w )
ptr_z     = conv_numpy_double_to_ptr( z )
ptr_ldz   = conv_numpy_int32_to_ptr( ldz )
ptr_wk    = conv_numpy_double_to_ptr( wk )
ptr_info  = conv_numpy_int32_to_ptr( info )

######################
######################
######################
id = 0
for i in range( nsize ):
    line = sys.stdin.readline()
    str  = line[:-1].split()
    ap[ id ] = float( str[ 2 ] )
    bp[ id ] = float( str[ 3 ] )
    id = id + 1

print( "input:" )
print( "ndim = %4d" % ( ndim ) )
for i in range( nsize ):
	print( "%4d: %16.2f%16.2f" % ( i, ap[ i ], bp[ i ] ) )

########################################
wrap_dspgv.liblapack.dspgv_( ptr_itype, ptr_jobz, ptr_uplo, ptr_n, ptr_ap, ptr_bp, ptr_w, ptr_z, ptr_ldz, ptr_wk, ptr_info )

########################################
print( "retval: %4d" % ptr_info[ 0 ] )
print( "eigen values and vectors:" )
sys.stdout.write( "%4s" % "" )
for i in range( ndim ):
	sys.stdout.write( "%11d" % i )
print( "" )

sys.stdout.write( "%4s" % "E" )
for i in range( ndim ):
	sys.stdout.write( "%11.4f" % w[ i ] )
print( "" )
for j in range( ndim ):
    sys.stdout.write( "%4d" % j )
    for i in range( ndim ):
	    sys.stdout.write( "%11.4f" % z[ j * ndim + i ] )
    print( "" )
