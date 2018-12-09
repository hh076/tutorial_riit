import ctypes, wrap_sort

nelem = 10
array_data = [ (  4, -3.38e+00 ), (  7, -9.29e+00 ), ( 20,  1.38e+00 ), ( -9,  8.02e+00 ),
               ( 77,  1.33e+00 ), ( -3,  3.30e+00 ), ( 13, -4.30e+00 ), ( -5,  5.00e+00 ),
               ( 10,  7.90e+00 ), (  1,  3.30e+00 ) ]

nelem_c     = ctypes.c_int32( nelem )
ptr_nelem   = ctypes.byref( nelem_c )
structarray = (wrap_sort.STRUCT_ELEM * nelem)( *array_data )

print( "Before sort:" )
for i in range( nelem ):
    print( "%4d: %6d%16.2e" % ( i, structarray[ i ].key, structarray[ i ].value ) )

wrap_sort.libsort.bsortc_struct( nelem_c, structarray )
#wrap_sort.libsort.__mysort_MOD_bsortf95_struct( ptr_nelem, structarray )
#wrap_sort.libsort._Z15bsortcpp_structiP11key_value_t( nelem_c, structarray )

print( "After  sort:" )
for i in range( nelem ):
    print( "%4d: %6d%16.2e" % ( i, structarray[ i ].key, structarray[ i ].value ) )
