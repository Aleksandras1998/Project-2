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
        sum_start=0
        sum_end=Nx-DeltaX
        for x in range (sum_start,sum_end+1):
            for y in range (0,Ny):
                for z in range (0,Nz):
                    array=array_from_file[x,y,z]*array_from_file[x+DeltaX,Yref,Zref]
                    print(array)
                    sum_array=array[sum_start:sum_end+1]
                    Cr_cor=np.sum(sum_array)/(Nx-DeltaX)
        return Cr_cor
        

    
    #return result