#include <stdio.h>
#include <unistd.h>
#include <mpi.h>

int main ( int argc, char **argv )
{
    int nprocs, myid ;
    int len ;
    char name[ BUFSIZ ] ;
    char str_name[ BUFSIZ ] ;

    MPI_Init ( &argc, &argv ) ;
    MPI_Comm_rank ( MPI_COMM_WORLD, &myid ) ;
    MPI_Comm_size ( MPI_COMM_WORLD, &nprocs ) ;

    MPI_Get_processor_name( name, &len ) ;
    gethostname( str_name, sizeof( str_name ) ) ;

    fprintf ( stdout, "nproc: %d -> id: %d : %4d, %s, %s\n", nprocs, myid, len, name, str_name ) ;

    MPI_Finalize ( ) ;
    return 0 ;
}
