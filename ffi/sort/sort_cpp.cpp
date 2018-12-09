#include <cstdio>
#include <cstdlib>
#include "sort_c.h"

int bsortcpp_array( int n, int *keys, double *values )
{
    int i, j ;
    int itmp ;
    double tmp ;
    
///    fprintf( stdout, "nelem: %4d\n", n ) ;
///    for ( i = 0 ; i < n ; i++ ) {
///        fprintf( stdout, "b: %4d%6d%16.2e\n", i, keys[ i ], values[ i ] ) ;
///    }
    for ( i = 0 ; i < n - 1 ; i++ ) {
        for ( j = n - 1 ; j > i ; j-- ) {
            if ( keys[ j - 1 ] > keys[ j ] ) {
                itmp            = keys[ j - 1 ] ;
                keys[ j - 1 ]   = keys[ j ] ;
                keys[ j ]       = itmp ;
                tmp             = values[ j - 1 ] ;
                values[ j - 1 ] = values[ j ] ;
                values[ j ]     = tmp ;
            }
        }
    }
///    for ( i = 0 ; i < n ; i++ ) {
///        fprintf( stdout, "a: %4d%6d%16.2e\n", i, keys[ i ], values[ i ] ) ;
///    }
    return 0 ;
}

int bsortcpp_struct( int n, key_value_t *array )
{
    int i, j ;
    key_value_t tmp ;
///    fprintf( stderr, "nelem: %4d\n", n ) ;
///    for ( i = 0 ; i < n ; i++ ) {
///        fprintf( stderr, "b: %4d%6d%16.2e\n", i, array[ i ].key, array[ i ].value ) ;
///    }
    for ( i = 0 ; i < n - 1 ; i++ ) {
        for ( j = n - 1 ; j > i ; j-- ) {
            if ( array[ j - 1 ].key > array[ j ].key ) {
                tmp            = array[ j - 1 ] ;
                array[ j - 1 ] = array[ j ] ;
                array[ j ]     = tmp ;
            }
        }
    }
///    for ( i = 0 ; i < n ; i++ ) {
///        fprintf( stderr, "b: %4d%6d%16.2e\n", i, array[ i ].key, array[ i ].value ) ;
///    }
    return 0 ;
}
