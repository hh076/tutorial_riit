import ctypes

libsort = ctypes.CDLL( "./libsort.so" )
#libsort = ctypes.CDLL( "./libsort.dylib" )

#Typename Aliases
T_INT        = ctypes.c_int32
T_PTR_VOID   = ctypes.c_void_p
T_PTR_INT    = ctypes.POINTER( ctypes.c_int32  )
T_PTR_DOUBLE = ctypes.POINTER( ctypes.c_double )

class STRUCT_ELEM( ctypes.Structure ):
    _fields_ = [( "key", ctypes.c_int ), ( "value", ctypes.c_double )]
    def __init__(self, key, value):  
        self.key   = key
        self.value = value

T_PTR_STRUCT = ctypes.POINTER( STRUCT_ELEM )

###### Type information for all required functions ######
### array ###
libsort.bsortf_.restype  = T_PTR_VOID
libsort.bsortf_.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]

libsort.bsortc_array.restype  = T_INT
libsort.bsortc_array.argtypes = [ T_INT, T_PTR_INT, T_PTR_DOUBLE ]

libsort.__mysort_MOD_bsortf95_array.restype  = T_PTR_VOID
libsort.__mysort_MOD_bsortf95_array.argtypes = [ T_PTR_INT, T_PTR_INT, T_PTR_DOUBLE ]

libsort._Z14bsortcpp_arrayiPiPd.restype  = T_INT
libsort._Z14bsortcpp_arrayiPiPd.argtypes = [ T_INT, T_PTR_INT, T_PTR_DOUBLE ]

### struct ###
libsort.bsortc_struct.restype   = T_INT
libsort.bsortc_struct.argtypes  = [ T_INT, T_PTR_STRUCT ]

libsort.__mysort_MOD_bsortf95_struct.restype  = T_PTR_VOID
libsort.__mysort_MOD_bsortf95_struct.argtypes = [ T_PTR_INT, T_PTR_STRUCT ]

libsort._Z15bsortcpp_structiP11key_value_t.restype  = T_INT
libsort._Z15bsortcpp_structiP11key_value_t.argtypes = [ T_INT, T_PTR_STRUCT ]
