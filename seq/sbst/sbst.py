import sys,re

if len( sys.argv ) <= 2 :
    sys.exit( "Error: len(args) <= 2: args: %s" % sys.argv )

rstr = sys.argv[ 1 ]
sstr = sys.argv[ 2 ]

if len( sys.argv ) <= 3:
    fin = sys.stdin
else:
    filename = sys.argv[ 3 ]
    fin = open( filename, 'r' )

#########################################
for line in fin:
    iline = line[:-1]
    oline = re.sub( rstr, sstr, iline )
    print( oline )

#########################################
fin.close()
