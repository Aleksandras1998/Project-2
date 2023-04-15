import numpy as np

def dataLoad(filename, Nx, Ny, Nz):
    
    with open(filename, mode='rb') as file: # b is important -> binary
        filein = file.read()
         
    #Convert binary data to a numpy array of single-precision floats
    data=np.frombuffer(filein, dtype=np.float32)
    
    #Reshape the array into the desired dimensions
    data=np.reshape(data, (Nz, Ny, Nx))    

    return data