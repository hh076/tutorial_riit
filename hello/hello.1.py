for i in range( 5 ):
    print( "%16.4e" % ( float( i ) / 3 ) )

array = [ 5.7, 7.8, 9.10, 7.95 ]
print( "Length of array: %d" % len( array ) )
for v in array:
    print( "%16.4f" % (v - array[ 0 ]) )
