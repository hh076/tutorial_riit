import sys, numpy, scipy
from scipy import linalg

##################################################
##################################################
##################################################

line = sys.stdin.readline()
str  = line[:-1].split()
ndim = int( str[ 0 ] )
nsol = int( str[ 1 ] )

A  = numpy.empty( [ ndim, ndim ], dtype=numpy.float64 )
B  = numpy.empty( [ nsol, ndim ], dtype=numpy.float64 )
X  = numpy.empty( [ nsol, ndim ], dtype=numpy.float64 )

for icol in range( ndim ):
    strs = sys.stdin.readline()[:-1].split()
    for irow in range( ndim ):
        A[ icol ][ irow ] = float( strs[ irow ] )

for icol in range( nsol ):
    strs = sys.stdin.readline()[:-1].split()
    for irow in range( ndim ):
        B[ icol ][ irow ] = float( strs[ irow ] )

############
############
############
print( "ndim, nsol = %4d %4d" % ( ndim, nsol ) )
print( "A:" )
for icol in range( ndim ):
    for irow in range( ndim ):
        sys.stdout.write( "%16.4f" % A[ icol ][ irow ] )
    sys.stdout.write( "\n" )
print( "B:" )
for irow in range( ndim ):
    for isol in range( nsol ):
        sys.stdout.write( "%16.4f" % B[ isol ][ irow ] )
    sys.stdout.write( "\n" )

##################################################
##################################################
##################################################
LU, PIV = scipy.linalg.lu_factor( A )
#print( LU )
for isol in range( nsol ):
    X[ isol ] = scipy.linalg.lu_solve( (LU, PIV), B[ isol ] )

############
############
############
print( "ANS:" )
for irow in range( ndim ):
    for isol in range( nsol ):
        sys.stdout.write( "%16.4f" % X[ isol ][ irow ] )
    sys.stdout.write( "\n" )
