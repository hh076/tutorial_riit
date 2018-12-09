      program main
      implicit none
      integer i, nelem, keys( 10 )
      double precision values ( 10 )
      data keys/ 4, 7, 20, -9, 77, -3, 13, -5, 10, 1 / 
      data values/ -3.38d0, -9.29d0,  1.38d0,  8.02d0,  1.33d0,
     &              3.30d0, -4.30d0,  5.00d0,  7.90d0,  3.30d0 /
cc
      nelem = 10
      do i = 1, nelem
          write( *, '(i10, f16.2)' ) keys( i ), values( i )
      enddo

      call bsortf( nelem, keys, values )

      do i = 1, nelem
          write( *, '(i10, f16.2)' ) keys( i ), values( i )
      enddo
cc
      end
