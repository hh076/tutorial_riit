      program main
      implicit none
      character jobz, uplo
      integer   i, j, ndim, itype, ldz, info, idummy
      double precision ap( 100 * 100 ), bp( 100 * 100 )
      double precision  w( 100 * 100 ),  z( 100 * 100 ), wk( 100 * 100 )
c
      itype = 1
      jobz = 'V'
      uplo = 'U'
      read( *, * ) ndim
      write( *, * ) 'ndim:', ndim
      do i = 1, ( ndim * ( ndim + 1 ) ) / 2
         read( *, * ) idummy, idummy, ap( i ), bp( i )
      enddo
c
      write( *, * ) 'input upper triangular matrices A, B:'
      do i = 1, ( ndim * ( ndim + 1 ) ) / 2
         write( *, '(i4,2f8.2)' ) i, ap( i ), bp( i )
      enddo
c
      ldz = ndim
      call dspgv( itype, jobz, uplo, ndim, ap, bp, w, z, ldz, wk, info )
c
      write( *, * ) 'retval: ', info
      write( *, * ) 'eigen values and vectors:'
      write( *, '(a4,4i11)' ) '', ( i, i = 1, 4 )
      write( *, '(a4,4f11.4)' ) 'E', ( w( i ), i = 1, 4 )
      do j = 1, ndim
         write( *, '(i4,4f11.4)' )
     &                     j, ( z( ( j - 1 ) * ndim + i ), i = 1, ndim )
      enddo
c
      end
