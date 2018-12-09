import sys, numpy
from mpi4py import MPI

##########################################
##########################################
##########################################
comm   = MPI.COMM_WORLD
myrank = MPI.COMM_WORLD.Get_rank()
nprocs = MPI.COMM_WORLD.Get_size()
root   = 0

##########################################
##########################################
##########################################
nsize = 10000
array = numpy.empty( [ nsize ], numpy.float64 )
for i in range( nsize ):
	array[ i ] = 3.938e-04 + ( i + 1 ) * 4 * ( myrank + 1 )

##########################################
##########################################
##########################################
if ( myrank == root ):
    print( "Before reduce:" )
    print( "Nproc, rank = %10d%10d" % ( nprocs, myrank ) )
    print( "%16.8e, %16.8e" % ( array[ 0 ], array[ nsize - 1 ] ) )

##########################################
##########################################
##########################################
garray = comm.reduce( array, MPI.SUM, root )

if ( myrank == root ):
    print( "After  reduce:" )
    print( "Nproc, rank = %10d%10d" % ( nprocs, myrank ) )
    print( "%16.8e, %16.8e" % ( garray[ 0 ], garray[ nsize - 1 ] ) )
