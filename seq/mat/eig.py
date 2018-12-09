import sys, numpy, scipy
from scipy import linalg

line = sys.stdin.readline()
str  = line[:-1].split()
ndim = int( str[ 0 ] )

A = numpy.empty( [ ndim, ndim ], dtype=numpy.float64 )
B = numpy.empty( [ ndim, ndim ], dtype=numpy.float64 )

id = 0
for icol in range( ndim ):
    strs = sys.stdin.readline()[:-1].split()
    for irow in range( ndim ):
        A[ icol ][ irow ] = float( strs[ irow ] )

for icol in range( ndim ):
    strs = sys.stdin.readline()[:-1].split()
    for irow in range( ndim ):
        B[ icol ][ irow ] = float( strs[ irow ] )

print( "Debug print:" )
print( "ndim = %4d" % ( ndim ) )
print( "A:\n%s" % A )
print( "B:\n%s" % B )

evals, evecs = scipy.linalg.eigh( A, b=B, lower=False, type=1 )

print( "eigen values and vectors:" )
sys.stdout.write( "%4s" % "" )
for i in range( ndim ):
    sys.stdout.write( "%11d" % i )
print( "" )

sys.stdout.write( "%4s" % "E" )
for i in range( ndim ):
    sys.stdout.write( "%11.4f" % evals[ i ] )
print( "" )
for j in range( ndim ):
    sys.stdout.write( "%4d" % j )
    for i in range( ndim ):
        sys.stdout.write( "%11.4f" % evecs[ i ][ j ] )
    print( "" )
