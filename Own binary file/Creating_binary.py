import numpy as np

Nz, Ny, Nx= 4,5,6
data=np.random.rand(Nx, Ny, Nz).astype(np.float32)

#Save the 3D array as a binary file
filename='small 3D array.bin'

with open(filename,'wb') as file:
    file.write(data.tobytes())
    

