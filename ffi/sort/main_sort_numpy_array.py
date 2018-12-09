import ctypes, wrap_sort, numpy

keys_data   = [ 4, 7, 20, -9, 77, -3, 13, -5, 10, 1 ]
values_data = [ -3.38e0, -9.29e0,  1.38e0,  8.02e0,  1.33e0,
                 3.30e0, -4.30e0,  5.00e0,  7.90e0,  3.30e0 ]

nelem  = 10
nelemc = ctypes.c_int32( nelem )
n      = numpy.array( [ nelem ],   dtype = numpy.int32 ) 
keys   = numpy.array( keys_data,   dtype = numpy.int32 ) 
values = numpy.array( values_data, dtype = numpy.float64 )

ptr_nelem  = n.ctypes.data_as( wrap_sort.T_PTR_INT )
ptr_keys   = keys.ctypes.data_as( wrap_sort.T_PTR_INT )
ptr_values = values.ctypes.data_as( wrap_sort.T_PTR_DOUBLE )

print( "Before sort:" )
for i in range( keys.size ):
	print( "%4d: %6d%16.2e" % ( i, keys[ i ], values[ i ] ) )

wrap_sort.libsort.bsortf_( ptr_nelem, ptr_keys, ptr_values )
#wrap_sort.libsort.bsortc_array( nelemc, ptr_keys, ptr_values )
#wrap_sort.libsort.__mysort_MOD_bsortf95_array( ptr_nelem, ptr_keys, ptr_values )
#wrap_sort.libsort._Z14bsortcpp_arrayiPiPd( nelemc, ptr_keys, ptr_values )

print( "After  sort:" )
for i in range( keys.size ):
	print( "%4d: %6d%16.2e" % ( i, keys[ i ], values[ i ] ) )

