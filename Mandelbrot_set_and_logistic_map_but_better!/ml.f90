program ml

		integer, parameter :: pixel_density = 500 !Pixel density is linear
		integer, parameter :: num_it = 500 !How picky do you want to be?
		integer, parameter :: num_l = 500 !resolution  on z axis
		real :: xmin, xmax, ymin, ymax ! Boundries
		real :: xx,yy,zz !points belonging to the Mandelbrot set! 
		real :: xx0,yy0 !ausiliaries!
		real :: verify 
		integer :: i, j, k, n !


			    xmin = -2.0
			    xmax = 1.0
			    ymin = -1.5
			    ymax = 1.5
			   


					    ! Open a file to write data
					    open(unit=10, file='ml.dat', status='replace')

					    do i = 1, pixel_density ! Resolution
						
						x = xmin + (i-1) * ((xmax-xmin)/pixel_density)
								
								do j = 1, pixel_density
									
									y = ymin + (j-1) * ((ymax-ymin)/pixel_density)
									
									xx=0
									yy=0
									
									
									xx0=0
									yy0=0
									
									
									do k = 1 , num_it !eliminating useless points!
										
											
											xx=(xx0**2)-(yy0**2)+x
											yy=(2*xx0*yy0)+y
											
											verify= (xx**2)+(yy**2)
													
											if (verify>4) then
											
											exit																	
														
											end if
											
											xx0= xx
											yy0= yy	
									end do 	
									
									
										if (verify<4) then
											
											xx=0
											yy=0
											
											
											xx0=0
											yy0=0
											
											do n= 1, num_l !getting z coordinates
											
														xx=(xx0**2)-(yy0**2)+x
														yy=(2*xx0*yy0)+y
																
														xx0= xx				
														yy0= yy							
															
														z=xx
																			
														write(10, *) x, y, z						
													
													
											end do
														
										end if
								end do
						
					    end do
	    call system("gnuplot ml.gnu") ! HERE WE FINALLY PLOT!
	    
end program ml


