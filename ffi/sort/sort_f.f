      subroutine bsortf( n, keys, values )
      implicit none
      integer n
      integer keys( n )
      double precision values( n )
      integer i, j, itmp
      double precision dtmp
c     do i = 1, n
c        write( *, * ) i, keys( i ), values( i )
c     enddo
      do i = 1, n-1, +1
         do j = n, i+1, -1
            if ( keys( j - 1 ) .gt. keys( j ) ) then
               itmp            = keys( j - 1 )
               keys( j - 1 )   = keys( j )
               keys( j )       = itmp
               dtmp            = values( j - 1 )
               values( j - 1 ) = values( j )
               values( j )     = dtmp
            endif
         enddo
      enddo
c     do i = 1, n
c        write( *, * ) i, keys( i ), values( i )
c     enddo
      end
