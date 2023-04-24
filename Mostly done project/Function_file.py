import numpy as np
from Data_loader import Yref,Zref

def dataLoad(filename, Nx, Ny, Nz):
     
    num_elements=Nx*Ny*Nz
    
    #Read data from the binary file
    #print(filein)
    values = np.fromfile("turbine_32x32x8192.bin", dtype=np.float32)
    
    #Checking if the number of elements in the file 
    #matches the num_elements
    
    num_file=len(values) 
    if num_file != num_elements:
        print(f'Error: Number of elements in the {filename} file\n'+
                f'({num_file}) does not match the expected number ({num_elements}))')
        return None
    else:
        print('╔' + '═'*49 + '╗\n'+
                f'║ Data loaded successfully from {filename} ║\n'+
                '╚' + '═'*49 + '╝')
    
    #Unpack the binary data into a flat array of floats
    #Reshape the array into a 3D array
    #data=np.reshape(values, (Nx,Ny, Nz)) #Nz come to the place of Nx (becomes as Nx)
    
    #data = np.zeros((Nz, Ny, Nx))
    #for x in range(Nx):
    #    for y in range(Ny):
    #        for z in range(Nz):
    #            data[z, y, x] = (values[(x * Ny * Nz) + (y * Nz) + z])
    original_data = np.reshape(values, (Nx, Ny, Nz))
    data = np.transpose(data, (2, 1, 0))

    print(data.shape)
    return data


def dataStatistics(data, statistic, Yref, Zref, DeltaX):
    
    #Import file
    array_from_file=data
    
# =============================================================================
# Creating if statements for stats calculations
# =============================================================================
    
    if statistic == "Mean":
        return np.round(np.mean(array_from_file, axis=0),2)
        
    if statistic == "Variance":
        mean=np.round(np.mean(array_from_file,axis=0),2)
        #print(mean)
        variance= (np.round(np.var(array_from_file,axis=0),2))
        #np.round(np.sum((array_from_file-mean)**2,axis=0)/array_from_file.shape[0],2)#Here can be problem with indexing
        #return np.round(np.sum((array_from_file-mean)**2,axis=0)/Nx,2)
        return variance
        
    if statistic == "Cross-correlation":
        if Yref is None or Zref is None or DeltaX is None:
            raise ValueError('Yref, Zref, and DeltaX must be provided for cross-correlation calculation')
        
        Nz, Ny, Nx = array_from_file.shape
        print(array_from_file.shape) #gives as output (4,5,6)=(Nz,Ny,Nx), which is incorrect. Has to be (6,5,4). Probably due to reshape function in the dataLoad
        
        lower_bound=1
        upper_bound=Nx-DeltaX
       

        
        #Creating an empty 2D array to store the multiplied elements
        multiply_array=np.zeros((Nx-DeltaX,Ny,Nz))
        print(multiply_array)
        
        for x in range (lower_bound,upper_bound):
            for y in range (Ny):
                for z in range (Nz):
                    multiply_array[x,y,z]=array_from_file[x,y,z]*array_from_file[x+DeltaX,Yref,Zref]
        print(np.round(multiply_array,4))
        summation=np.sum(multiply_array,axis=0)
        print()
        print(np.round(summation,4))
        

        return np.around(summation/(Nx-DeltaX),3)
        
  def dataPlot(data, statistic):
    
    
    #return result
        