set hidden3d
set isosample 40,40
set pm3d

# Set terminal to PNG with black background
set term pngcairo background "#000000" 

# Define custom palette with dark colors
set palette defined (0 "blue", \
                     0.1 "cyan", \
                     0.2 "green", \
                     0.3 "yellow", \
                     0.4 "orange", \
                     0.5 "red", \
                     0.6 "magenta", \
                     0.7 "purple", \
                     0.8 "brown", \
                     0.9 "dark-gray", \
                     0.95 "light-gray", \
                     1 "white")

# Set output file name
set output 'plot.png'

# Plot the data
splot 'ml.dat' using 1:2:3 with points pt 7 ps 0.01 lc palette

# Pause to view the plot (optional)
pause -1 "Press any key to continue"

# Reset terminal settings
set term pngcairo
