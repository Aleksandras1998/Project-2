import numpy as np
from Reading_binary import array_from_file
from Creating_binary import Nx, Ny, Nz


#small 3D array.bin

def dataStatistics(data, statistic, Yref, Zref, DeltaX):
    
    #Import file
    
    
    #Creating if statements for stats calculations
    if statistic == "Mean":
        
        return np.mean(array_from_file, axis=0)
        
    if statistic == "Variance":
        mean=np.round(np.mean(array_from_file,axis=0),2)
        print(mean)
        print (np.round(np.var(array_from_file,axis=0),2))
        return np.round(np.sum((array_from_file-mean)**2,axis=0)/Nx,2)
        
    if statistic == "Cross-correlation":
        lower_bound=0
        upper_bound=Nx-DeltaX

        
        #Creating an empty 2D array to store the multiplied elements
        multiply_array=np.zeros((Nx-DeltaX,Ny,Nz))
        
        for x in range (lower_bound,upper_bound):
            for y in range (Ny):
                for z in range (Nz):
                    multiply_array[x,y,z]=array_from_file[x,y,z]*array_from_file[x+DeltaX,Yref,Zref]
        print(np.round(multiply_array,4))
        summation=np.sum(multiply_array,axis=0)
        print()
        print(np.round(summation,4))
        

        return np.around(summation/(Nx-DeltaX),4)
        

    
    #return result