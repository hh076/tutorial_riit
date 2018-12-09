#include <stdio.h>
#include <stdlib.h>

void dspgv_( int *itype, char *jobz, char *uplo, int *ndim,
             double *ap, double *bp, double *w, double *z, int *ldz, double *wk, int *info ) ;

int main()
{
    char  jobz, uplo ;
    int   i, j, ndim, nelem_tri, nelem_sq, itype, ldz, info, idummy ;
    double *ap, *bp, *w, *z, *wk ;
    char buf[ BUFSIZ ] ;
///
    itype = 1 ;
    jobz = 'V' ;
    uplo = 'U' ;
///
    fgets( buf, sizeof( buf ), stdin ) ; 
    sscanf( buf, "%d", &ndim ) ;
    nelem_tri = ( ndim * ( ndim + 1 ) ) / 2 ;
    nelem_sq  = ndim * ndim ;
    fprintf( stdout, "%4d%4d%4d\n", ndim, nelem_tri, nelem_sq ) ;
///
    ap = ( double * )malloc( nelem_tri * sizeof( double ) ) ;
    bp = ( double * )malloc( nelem_tri * sizeof( double ) ) ;
    w  = ( double * )malloc( ndim      * sizeof( double ) ) ;
    z  = ( double * )malloc( nelem_sq  * sizeof( double ) ) ;
    wk = ( double * )malloc( ndim * 3  * sizeof( double ) ) ;
///
    for ( i = 0 ; i < nelem_tri ; i++ ) {
        fgets( buf, sizeof( buf ), stdin ) ; 
        sscanf( buf, "%d%d%lf%lf", &idummy, &idummy, &(ap[ i ]), &(bp[ i ]) ) ;
    }
///
    fprintf( stdout, "input upper triangular matrices A, B:\n" ) ;
    for ( i = 0 ; i < nelem_tri ; i++ ) {
        fprintf( stdout, "%4d%8.2f%8.2f\n", i, ap[ i ], bp[ i ] ) ;
    }
///
    ldz = ndim ;
    dspgv_( &itype, &jobz, &uplo, &ndim, ap, bp, w, z, &ldz, wk, &info ) ;
///
    fprintf( stdout, "retval: %4d\n", info ) ;
    fprintf( stdout, "eigen values and vectors:\n" ) ;
    fprintf( stdout, "    " ) ;
    for ( i = 0 ; i < 4 ; i++ ) {
        fprintf( stdout, "%11d", i ) ;
    }
    fprintf( stdout, "\n" ) ;
    fprintf( stdout, "   E" ) ;
    for ( i = 0 ; i < 4 ; i++ ) {
        fprintf( stdout, "%11.4f", w[ i ] ) ;
    }
    fprintf( stdout, "\n" ) ;
    for ( j = 0 ; j < 4 ; j++ ) {
        fprintf( stdout, "%4d", j ) ;
        for ( i = 0 ; i < 4 ; i++ ) {
            fprintf( stdout, "%11.4f", z[ j * ndim + i ] ) ;
        }
        fprintf( stdout, "\n" ) ;
    }
    free( ap ) ;
    free( bp ) ;
    free( w  ) ;
    free( z  ) ;
    free( wk ) ;
///
    return 0 ;
}
