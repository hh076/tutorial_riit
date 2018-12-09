#include <stdio.h>
#include "sort_c.h"

int nelem = 10 ;
key_value_t array[] = {
    {   4,  -3.38e0 },
    {   7,  -9.29e0 },
    {  20,   1.38e0 },
    {  -9,   8.02e0 },
    {  77,   1.33e0 },
    {  -3,   5.30e0 },
    {  13,  -4.30e0 },
    {  -5,   5.00e0 },
    {  10,   7.90e0 },
    {   1,   3.30e0 }
} ;

int main()
{
    int i ;
    for ( i = 0 ; i < nelem ; i++ ) {
        fprintf( stdout, "%10d%16.2f\n", array[ i ].key, array[ i ].value ) ;
	}

    bsortc_struct( nelem, array ) ;

    for ( i = 0 ; i < nelem ; i++ ) {
        fprintf( stdout, "%10d%16.2f\n", array[ i ].key, array[ i ].value ) ;
	}
    return 0 ;
}
