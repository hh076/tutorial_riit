import sys

def sum1( arr ):
    s_even = 0
    s_odd  = 0
    for i in range( len( arr ) ):
        if ( (i % 2) == 0 ):
            s_even = s_even + arr[ i ] * 2
        else:
            s_odd  = s_odd  + arr[ i ] * 3
    return s_even, s_odd

array = [5.7, 7.8, 9.10, 7.95]
s_even, s_odd = sum1( array )

sys.stdout.write( "test: " )
print( "sum1 of %s -> %8.2f,%8.2f" % ( array, s_even, s_odd ) )
