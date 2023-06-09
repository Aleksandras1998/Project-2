import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dataLoad(filename, Nx, Ny, Nz):
    
    input_num_elements=Nx*Ny*Nz
    
    with open(filename, mode='rb') as file:
        
        #Read data from the binary file
        array_1d=np.fromfile(file,dtype=np.single)
        
        #Checking if the number of elements in the file 
        #matches the number of elements from input
        
        num_elements_in_file=array_1d.size

        if num_elements_in_file != input_num_elements:
            print(f'Error: Number of elements in the {filename} file\n'+
                  f'({num_elements_in_file}) does not match the expected number ({input_num_elements}))')
            return None
        else:
            print('╔' + '═'*49 + '╗\n'+
                 f'║ Data loaded successfully from {filename} ║\n'+
                 f'║ The number of elements in {filename} is: {num_elements_in_file} ║\n'+
                  '╚' + '═'*49 + '╝')
            
        
        
        #Reshape the 1D array into the 3D array according the rules given
        #for z in range (Nz):
           # for y in range(Ny):
               # for x in range(Nx):
                   # index_1d=z+y*Nz+x*Ny*Nz
                   # array_3d[z,y,x]=array_1d[index_1d]
        # data=array_3d

        #Reshape the 1D array into the 3D array according the rules given
        data=array_1d.reshape((Nx, Ny, Nz))
        data=np.transpose(data, (2, 1, 0)) 
            

     
        return data


def dataStatistics(data, statistic, Yref=None, Zref=None, DeltaX=None):
    
    #Reshaping [Nz x Ny x Nx] array to [Nx x Ny x Nz] for further stats calculations
    data=data.transpose((2,1,0))
    results=np.zeros((data.shape[1], data.shape[2]))
    # print(data)
    # print(array_yz)
    Nx, Ny, Nz = data.shape

# =============================================================================
#                   Creating if statements for stats calculations
# =============================================================================
    
    if statistic == "Mean":
        results = np.round(np.mean(data, axis=0),3)       
# =============================================================================
#         Alternative option for mean calculation (gives same result):
# =============================================================================
        # for y in range(data.shape[1]):
        #     for z in range(data.shape[2]):
        #         array_yz[y,z] = np.mean(data[:,y,z])
        # mean_yz=array_yz
        # return mean_yz
        

       
    if statistic == "Variance":
        results = np.round(np.var(data,axis=0),3)  
    
# =============================================================================
#         Alternative option for variance calculation (gives same result):
# =============================================================================
        # for y in range(data.shape[1]):
        #     for z in range(data.shape[2]):
        #         array_yz[y,z] = np.mean(data[:,y,z])
        # mean_yz=array_yz
        # variance_yz=np.sum((data-mean_yz)**2,axis=0)/data.shape[0]
        # return variance_yz
        
               
        
    if statistic == "Cross-correlation":
        if Yref is None or Zref is None or DeltaX is None:
            raise ValueError('Yref, Zref, and DeltaX must be provided for cross-correlation calculation')
        
        #Assigning variables for cross-correlation calculations
       
        lower_bound=1
        upper_bound=Nx-DeltaX
        print(data.shape[0])
        print(data.shape[1])
        print(data.shape[2])

        
        #Creating an empty 3D array to store multiplied elements
        multiply_array=np.zeros((Nx-DeltaX,Ny,Nz))
        
        for x in range (lower_bound,upper_bound):
            for y in range (Ny):
                for z in range (Nz):
                    multiply_array[x,y,z]=data[x,y,z]*data[x+DeltaX,Yref,Zref]
        summation=np.sum(multiply_array,axis=0)      

        results =  np.round(summation/(Nx-DeltaX),3)
    assert results.shape == (Ny, Nz), (f'Error: {statistic} has invalid shape')
    return results

def dataPlot (data, statistic):
    
# =============================================================================
# [1]-Contour plots
# =============================================================================
    if statistic == 'Mean':
        
        print('Mean plot has been successfully generated. Continue if needed or enter [4]')
        
        #Creating x, y coordiantes for the contour plot
        x=np.arange(data.shape[1])
        y=np.arange(data.shape[0])
        X,Y=np.meshgrid(x,y)
        
        #Creating the contour plot
        fig,ax=plt.subplots()
        contour=ax.contourf(X,Y, data)
        fig.colorbar(contour)
        
        #Setting the title and axis labels
        ax.set_title(f'Contour Plot of Mean array with size {data.shape[0]}x{data.shape[1]}')
        ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
        ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
        #Show the plot
        plt.show(block=False)
        
        
        return (dataPlot)
    
    if statistic == 'Variance':
        
        print('Variance plot has been successfully generated. Continue if needed or enter [4]')
        
        #Creating x, y coordiantes for the contour plot
        x=np.arange(data.shape[1])
        y=np.arange(data.shape[0])
        X,Y=np.meshgrid(x,y)
        
        #Creating the contour plot
        fig,ax=plt.subplots()
        contour=ax.contourf(X,Y, data)
        fig.colorbar(contour)
        
        #Setting the title and axis labels
        ax.set_title(f'Contour Plot of Variance array with size {data.shape[0]}x{data.shape[1]}')
        ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
        ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
        #Show the plot
        plt.show(block=False)
        
        
        return (dataPlot)
    
    if statistic == 'Cross-Correlation':
        
        print('Cross-Correlation plot has been successfully generated. Continue if needed or enter [4]')
        
        #Creating x, y coordiantes for the contour plot
        x=np.arange(data.shape[1])
        y=np.arange(data.shape[0])
        X,Y=np.meshgrid(x,y)
        
        #Creating the contour plot
        fig,ax=plt.subplots()
        contour=ax.contourf(X,Y, data)
        fig.colorbar(contour)
        
        #Setting the title and axis labels
        ax.set_title(f'Contour Plot of Cross-correlation array with size {data.shape[0]}x{data.shape[1]}')
        ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
        ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
        #Show the plot
        plt.show(block=False)
        
        return (dataPlot)

# =============================================================================
# [2] - Surface Plot:
# =============================================================================

    # if statistic == 'Mean':
        
    #     #Creating x, y coordiantes for the contour plot
    #     x=np.arange(data.shape[1])
    #     y=np.arange(data.shape[0])
    #     X,Y=np.meshgrid(x,y)
        
    #     #Creating the surface plot
    #     fig=plt.figure()
    #     ax=fig.add_subplot(111,projection='3d')
    #     surf=ax.plot_surface(X, Y, data, cmap='coolwarm')
    #     fig.colorbar(surf)
        
    #     #Setting the title and axis labels
    #     ax.set_title(f'Surface Plot of Mean array with size {data.shape[1]}x{data.shape[0]}')
    #     ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    #     ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
    #     ax.set('Value')
        
    #     #Show the plot
    #     plt.show()
        
    #     return (dataPlot)
    
    # if statistic == 'Variance':
        
    #     #Creating x, y coordiantes for the contour plot
    #     x=np.arange(data.shape[1])
    #     y=np.arange(data.shape[0])
    #     X,Y=np.meshgrid(x,y)
        
    #     #Creating the surface plot
    #     fig=plt.figure()
    #     ax=fig.add_subplot(111,projection='3d')
    #     surf=ax.plot_surface(X, Y, data, cmap='coolwarm')
    #     fig.colorbar(surf)
        
    #     #Setting the title and axis labels
    #     ax.set_title(f'Surface Plot of Variance array with size {data.shape[1]}x{data.shape[0]}')
    #     ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    #     ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
    #     ax.set('Value')
        
    #     #Show the plot
    #     plt.show()
        
    #     return (dataPlot)
    
    # if statistic == 'Cross-correlation':
        
    #     #Creating x, y coordiantes for the contour plot
    #     x=np.arange(data.shape[1])
    #     y=np.arange(data.shape[0])
    #     X,Y=np.meshgrid(x,y)
        
    #     #Creating the surface plot
    #     fig=plt.figure()
    #     ax=fig.add_subplot(111,projection='3d')
    #     surf=ax.plot_surface(X, Y, data, cmap='coolwarm')
    #     fig.colorbar(surf)
        
    #     #Setting the title and axis labels
    #     ax.set_title(f'Surface Plot of Cross-correlation array with size {data.shape[1]}x{data.shape[0]}')
    #     ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    #     ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
    #     ax.set('Value')
        
    #     #Show the plot
    #     plt.show()
        
    #     return (dataPlot)     
        

        