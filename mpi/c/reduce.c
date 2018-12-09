#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"

int main( int argc, char *argv[] )
{
    int    i, nsize,
           nprocs, myrank, root ;
    double *array, *array_sum ;

    MPI_Init( &argc, &argv ) ;
    MPI_Comm_size( MPI_COMM_WORLD, &nprocs ) ;
    MPI_Comm_rank( MPI_COMM_WORLD, &myrank ) ;

    root = 0 ;
    nsize = 10000 ;
    array     = ( double * )malloc( nsize * sizeof( double ) ) ;
    for ( i = 0 ; i < nsize ; i++ ) {
	    array[ i ] = 3.938e-04 + ( i + 1 ) * 4 * ( myrank + 1 ) ;
    }

    if ( myrank == root ) {
        array_sum = ( double * )malloc( nsize * sizeof( double ) ) ;
        printf( "Nproc = %10d\n", nprocs ) ;
        printf( "Before reduce:\n" ) ;
        printf( "%16.8e, %16.8e\n", array[ 0 ], array[ nsize - 1 ] ) ;
    }

    MPI_Reduce( array, array_sum, nsize, MPI_DOUBLE, MPI_SUM, root, MPI_COMM_WORLD ) ;

    if ( myrank == root ) {
        printf( "Nproc = %10d\n", nprocs ) ;
        printf( "After  reduce:\n" ) ;
        printf( "%16.8e, %16.8e\n", array_sum[ 0 ], array_sum[ nsize - 1 ] ) ;
        
    }
    
    free( array ) ;
    if ( myrank == root ) {
        free( array_sum ) ;
    }
    MPI_Finalize() ;
    return 0 ;
}
