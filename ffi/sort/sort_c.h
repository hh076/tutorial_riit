#ifndef __INCLUDE_SORT_C__
#define __INCLUDE_SORT_C__

typedef struct {
    int    key ;
    double value ;
} key_value_t ;

extern int bsortc_array ( int n, int *keys, double *values ) ;
extern int bsortc_struct( int n, key_value_t *array ) ;
extern int bsortcpp_array ( int n, int *keys, double *values ) ;
extern int bsortcpp_struct( int n, key_value_t *array ) ;

#endif
