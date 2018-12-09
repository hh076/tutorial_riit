import sys, ctypes
import wrap_sort

nelem = 10
keys_data   = [ 4, 7, 20, -9, 77, -3, 13, -5, 10, 1 ]
values_data = [ -3.38e0, -9.29e0,  1.38e0,  8.02e0,  1.33e0,
                 3.30e0, -4.30e0,  5.00e0,  7.90e0,  3.30e0 ]

nelem_c            = ctypes.c_int32( nelem )
ptr_nelem          = ctypes.byref( nelem_c )
keys_ctypesarray   = (ctypes.c_int32  * nelem)( *keys_data )
values_ctypesarray = (ctypes.c_double * nelem)( *values_data )

print( "Before sort:" )
for i in range( nelem ):
    print( "%4d: %6d%16.2e" % ( i, keys_ctypesarray[ i ], values_ctypesarray[ i ] ) )

wrap_sort.libsort.bsortf_( ptr_nelem, keys_ctypesarray, values_ctypesarray )
#wrap_sort.libsort.bsortc_array( nelem_c, keys_ctypesarray, values_ctypesarray )
#wrap_sort.libsort.__mysort_MOD_bsortf95_array( ptr_nelem, keys_ctypesarray, values_ctypesarray )
#wrap_sort.libsort._Z14bsortcpp_arrayiPiPd( nelem_c, keys_ctypesarray, values_ctypesarray )

print( "After  sort:" )
for i in range( nelem ):
    print( "%4d: %6d%16.2e" % ( i, keys_ctypesarray[ i ], values_ctypesarray[ i ] ) )
