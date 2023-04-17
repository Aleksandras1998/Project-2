import numpy as np
import struct
#from Data_loader import Nx, Ny, Nz

def dataLoad(filename, Nx, Ny, Nz):
     
    num_elements=Nx*Ny*Nz
    
    with open(filename, mode='rb') as file:
        #Read data from the binary file
        filein=file.read()
        #print(filein)
        
        #Checking if the number of elements in the file 
        #matches the num_elements
        
        num_file=len(filein)//4 # Each float is 4 bytes
        if num_file != num_elements:
            print(f'Error: Number of elements in the {filename} file\n'+
                  f'({num_file}) does not match the expected number ({num_elements}))')
            return None
        else:
            print('╔' + '═'*49 + '╗\n'+
                 f'║ Data loaded successfully from {filename} ║\n'+
                  '╚' + '═'*49 + '╝')
        
        #Unpack the binary data into a flat array of floats
        values=struct.unpack(f'{num_elements}f',filein)
        
        #Reshape the array into a 3D array
        data=np.reshape(values, (Nz,Ny, Nx)) #Nz come to the place of Nx (becomes as Nx)
     
        return data


def dataStatistics(data, statistic, Yref=None, Zref=None, DeltaX=None):
    
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
        #print (np.round(np.var(array_from_file,axis=0),2)) - works the same way as ↓
        #return np.round(np.sum((array_from_file-mean)**2,axis=0)/Nx,2)
        return np.round(np.sum((array_from_file-mean)**2,axis=0)/array_from_file.shape[0],2)#Here can be problem with indexing
        
    if statistic == "Cross-correlation":
        if Yref is None or Zref is None or DeltaX is None:
            raise ValueError('Yref, Zref, and DeltaX must be provided for cross-correlation calculation')
        
        Nx, Ny, Nz = array_from_file.shape
        print(array_from_file.shape) #gives as output (4,5,6)=(Nz,Ny,Nx), which is incorrect. Has to be (6,5,4). Probably due to reshape function in the dataLoad
        #Nx=array_from_file[2] 
        #Ny=array_from_file[1]
        #Nz=array_from_file[0]
        lower_bound=0
        upper_bound=Nx-DeltaX
        #print(Nx)
        #print(Ny)
        #print(Nz)

        
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
        

    
    #return result
        