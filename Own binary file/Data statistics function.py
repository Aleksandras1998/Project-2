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
        cross_cor=0.0
        
        #Creating an empty 2D array to store the multiplied elements
        multiply_array=np.zeros((Ny,Nz))
        
        for x in range (sum_start,sum_end):
            sum_arr=0.0
            for y in range (Ny):
                for z in range (Nz):
                    array=array_from_file[x,y,z]*array_from_file[x+DeltaX,Yref,Zref]
                    print(array)
                    sum_arr+=array
                    #print(sum_arr)
                                                                 
                     
                    # sum_array=array[sum_start:sum_end+1]
            Cr_cor=sum_arr/(Nx-DeltaX)
            cross_cor+=Cr_cor
        return cross_cor
        

    
    #return result