module mysort
  type keyvalue
    integer :: key
    double precision :: value
  end type keyvalue
contains
  subroutine bsortf95_array( n, keys, values )
    implicit none
    integer n
    integer keys( n )
    double precision values( n )
    integer i, j, itmp
    double precision dtmp
!
!   write( *, * ) 'nelem: ', n
!   do i = 1, n
!      write( *, * ) i, keys( i ), values( i )
!   enddo
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
!   do i = 1, n
!      write( *, * ) i, keys( i ), values( i )
!   enddo
  end subroutine bsortf95_array
!
  subroutine bsortf95_struct( n, array )
    implicit none
    integer n
    type( keyvalue ), dimension( n ) :: array
    type( keyvalue ) :: tmp
    integer i, j
!
!   write( *, * ) 'nelem: ', n
!   do i = 1, n
!      write( *, * ) i, array( i )%key, array( i )%value
!   enddo
    do i = 1, n-1, +1
      do j = n, i+1, -1
        if ( array( j - 1 )%key .gt. array( j )%key ) then
          tmp            = array( j - 1 )
          array( j - 1 ) = array( j )
          array( j )     = tmp
        endif
      enddo
    enddo
!   do i = 1, n
!      write( *, * ) i, array( i )%key, array( i )%value
!   enddo
  end subroutine bsortf95_struct
end module mysort
