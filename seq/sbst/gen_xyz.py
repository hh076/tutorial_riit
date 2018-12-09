import subprocess

python = "python"
#PYTHON = "python3"
Zs = [ "7.4", "8.3", "9.4" ]

comm = []
comm.append( python )
comm.append( "sbst.py" )
comm.append( "__ZZ__" )
comm.append( "" )
comm.append( "in.template" )

for i in range( len( Zs ) ):
    comm[ 3 ] = Zs[ i ]
    #print( "comm: %s" % comm )
    filename = "in.%s" % Zs[ i ]
    os = open( filename, "w" )
    print( "%s %s %s %s %s > %s" % ( comm[ 0 ], comm[ 1 ], comm[ 2 ], comm[ 3 ], comm[ 4 ], filename ) )
    subprocess.call( comm, stdout=os )
    os.close()
