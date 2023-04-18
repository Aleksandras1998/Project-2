

import struct
from matplotlib import pyplot as plt

import numpy as np
from Function_file import dataLoad


Nx = 8192
Ny = 32
Nz = 32

d = dataLoad("turbine_32x32x8192.bin", 8192, 32, 32)

#values = np.fromfile("turbine_32x32x8192.bin", dtype=np.float32)

z_slice = 15 # Choose the z-slice to plot

for x_s in range(1000, 1100):
    # Plot wind speeds for the chosen z-slice
    plt.imshow(d[:,:,x_s], cmap='jet') # Plot wind speeds as an image with jet colormap
    plt.colorbar(label='Wind Speed (m/s)') # Add colorbar with label
    plt.title(f'Wind Speeds at x = {x_s}') # Set title
    plt.xlabel('x') # Set x-axis label
    plt.ylabel('y') # Set y-axis label
    plt.show() # Show plot