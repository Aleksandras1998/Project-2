#turbine_32x32x8192.bin#
#Nz=32; Ny=32; Nx=8192
#Our goal is to reshape an 3D array, so that z would be the fastest-varying index(the lower number)
#followed by 'y' and slowest is x (8192)


import numpy as np
import struct

def dataLoad(filename, Nx, Ny, Nz):
    num_elements=Nx*Ny*Nz
    
    with open(filename, mode='rb') as file:
        #Read data from the binary file
        filein=file.read()
        
        #Checking if the number of elements in the file 
        #matches the num_elements
        
        num_file=len(filein)//4 # Each float is 4 bytes
        if num_file != num_elements:
            print(f'Error: Number of elements in the {filename} file\n'+
                  f'({num_file}) does not match the expected number ({num_elements}))')
            return None
        
        #Unpack the binary data into a flat array of floats
        values=struct.unpack(f'{num_elements}f',filein)
        
        #Reshape the array into a 3D array
        data=np.reshape(values, (Nz,Ny, Nx)) #Nz come to the place of Nx (becomes as Nx)
     
        return data

Nx = 2**10 #16384 #16384 #16384 #16384 #1024 = 2^10
Ny = 2**8 #32 #64 #128 #256 #128 = 2^7
Nz = 2**5  #16 #8 #4 #2 #64 = 2^6
filename = "turbine_32x32x8192.bin"

result = dataLoad(filename, Nx, Ny, Nz)
if result is not None:
    print(result)
    

#How to achieve the same result 8388608 by multiplying 3 different numbers:
# (2^10)*(2^7)*(2^6)=2^(10+7+6)=2^23 (sum of powers has to give always 23)
    

        