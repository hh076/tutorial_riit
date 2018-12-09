import sys,re

#########################################
def find_line( in_stream, str ):
    r = re.compile( str )
    for line in in_stream:
        #print( "find_line: %s" % line[:-1] )
        if ( r.search( line ) ):
            break
    return line

def skip_lines( in_stream, n ):
    i = 0
    for line in in_stream:
        if ( i >= n ):
            break
        #print( "skip_line: %s" % line[:-1] )
        i = i + 1
    return line

def read_split_lines( in_stream, n ):
    lines = []
    i = 0
    for line in in_stream:
        if ( i >= n ):
            break
        #print( "read_split_line: %s" % line[:-1] )
        strs = line[:-1].split()
        lines.append( strs )
        i = i + 1
    return lines

#def transpose_array2( array2 ):
#    array2_tr = [ [ None for i in range( len( array2 ) ) ] for i in range( len( array2[ 0 ] ) ) ]
#    for i in range( len( array2 ) ):
#        for j in range( len( array2[ 0 ] ) ):
#            array2_tr[ j ][ i ] = array2[ i ][ j ]
#    return array2_tr
#
#########################################
line = find_line( sys.stdin, "NUMB_AO, NSIZE_FOCK" )
strs = line[:-1].split()
na   = int( strs[ 3 ] )
print( "  na:\n%s : %d" % ( strs, na ) )

#########################################
line = find_line( sys.stdin, "TOTAL ENERGY =" )
strs = line[:-1].split()
total_ene_str = float( strs[ 3 ] )
print( " ene:\n%s : %e" % ( strs, float( total_ene_str ) ) )

#########################################
line  = find_line(  sys.stdin, "EIGEN VECTOR:" )
line  = skip_lines( sys.stdin, 1 )
eigen_values_str = line[:-1].split()
print( "eigen_values:\n%s" % eigen_values_str )

#########################################
#array2_tr = transpose_array2( lines )
##print( "array2_tr: %s" % array2_tr )
##print( "" )
#print( "NUMB_AO: %4d" % na )
#print( " ene: %s : %e" % ( strs, float( total_ene_str ) ) )
#norb = len( array2_tr ) - 1
#for i in range( norb ):
#    sys.stdout.write( "%4d:%13.8f" % ( i, float( egvs[ i + 1 ] ) ) )
#    for j in range( len( array2_tr[ 0 ] ) ):
#        sys.stdout.write( "%13.8f" % float( array2_tr[ i + 1 ][ j ] ) )
#    print( "" )
#########################################

eigen_vectors_tr_str = read_split_lines( sys.stdin, na )
print( "transposed 2dim list of eigenvalues:\n%s" % eigen_vectors_tr_str )
print( "" )

print( " ene: %12.4e" % float( total_ene_str ) )
for i in range( 4 ):
    sys.stdout.write( "%4d:" % ( i + 1 ) )
    for j in range( na ):
        sys.stdout.write( "%13s" % eigen_vectors_tr_str[ j ][ i + 1 ] )
    sys.stdout.write( "\n" )
