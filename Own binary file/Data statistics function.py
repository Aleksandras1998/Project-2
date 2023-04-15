import numpy as np
from Reading_binary import array_from_file
from Creating_binary import Nx


#small 3D array.bin

def dataStatistics(data, statistic):
    
    #Import file
    
    
    #Creating if statements for stats calculations
    if statistic == "Mean":
        
        return np.mean(array_from_file, axis=0)
        
    if statistic == "Variance":
        mean=np.round(np.mean(array_from_file,axis=0),2)
        print(mean)
        print (np.round(np.var(array_from_file,axis=0),2))
        return np.round(np.sum((array_from_file-mean)**2,axis=0)/len(Nx),2)
        
    # if statistic == "Cross-correlation":
    #     return np.std(statsdata[:,0])
        

    
    #return result