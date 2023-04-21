#small 3D array.bin Nx=6 Ny=5 Nz=4
#turbine_32x32x8192.bin Nx=8192 Ny=32 Nz=32

from Data_loader import dataLoader 
from Function_file import dataStatistics
import numpy as np

if __name__=='__main__':

# =============================================================================
#               Here we are creating User interaction Main menu
# =============================================================================
    
    data_loaded=False
    
    while True:
        
        try:
            user_input=int(input('┏' + '━'*33 + '┓\n'+
                                 '┃'+' '*4+'Your are now in Main menu'+' '*4+'┃\n'+
                                 '┃Please enter a number from 1 to 4┃\n'+
                                 '┗' + '━'*33 + '┛\n'+
                                 '[1] Load data.\n'+
                                 '[2] Display statistics.\n'+
                                 '[3] Generate plots.\n'+
                                 '[4] Quit.\n'+
                                 '>>'))
            if user_input >4 or user_input<1:
                #print()
                print('+'+'-'*40+'+')
                print('|' + ' '*16 + 'WARNING!' + ' '*16 + '|')
                raise ValueError('|' + ' '*3 + 'Select a number from the Main menu' + ' '*3 + '|')
        except ValueError as e:
            print(e)
            print('|' + ' '*12 + 'Please try again' + ' '*12 + '|')
            print('+' + '-'*40 + '+')
            
            continue
# =============================================================================
# [1]st selection-Uploading 3D array from binary file
# =============================================================================
        if user_input == 1:
            matrix_3d=dataLoader()
            print(np.round(matrix_3d,3))
            data_loaded=True

# =============================================================================
# [2]nd selection - Creating display for statistics
# =============================================================================
        elif user_input == 2:
            if not data_loaded:
                print()
                print('+'+'-'*40+'+\n'+
                      '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
                      '|' + ' '*3 + 'Please load data before continuing' + ' '*3 + '|\n'+
                      '+' + '-'*40 + '+')
            else:
                statistic = ['Mean','Variance','Cross-correlation'] #string of statistics
            
                while True:
                    user_input_statistic=int(input('┏' + '━'*40 + '┓\n'+
                                                   '┃Please select which statistic to display┃\n'+
                                                   '┗' + '━'*40 + '┛\n'+
                                                   "[1] Mean\n" +
                                                   "[2] Variance\n" +
                                                   "[3] Cross-correlation\n"  +
                                                   "[4] Return to the the main menu\n"+
                                                   ">>"))
                    if user_input_statistic ==1:
                        print()
                        print(f'The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:\n')
                        print(dataStatistics(matrix_3d, statistic[user_input_statistic - 1])) # have to figure out with Yref, Zref, DeltaX for first two statistics
                    elif user_input_statistic == 2:
                        print()
                        print(f'The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:\n')
                        print(dataStatistics(matrix_3d, statistic[user_input_statistic - 1]))
                    elif user_input_statistic == 3:
                        while True:
                            print('Please enter Yref, Zref, DeltaX values')
                            Yref=input('Yref: ').strip()
                            Zref=input('Zref: ').strip()
                            DeltaX=input('DeltaX: ').strip()
                            if Yref.isdigit() and Zref.isdigit() and DeltaX.isdigit():
                                Yref=int(Yref)
                                Zref=int(Zref)
                                DeltaX=int(DeltaX)
                                break
                            else:
                                print('Please enter integer values for Yref, Zref, and DeltaX.')
                        print()
                        print(f'The {statistic[user_input_statistic-1]} are:\n')
                        print(dataStatistics(matrix_3d, statistic[user_input_statistic - 1], Yref, Zref, DeltaX))
                        
                    elif user_input_statistic == 4:
                        break
                    else:
                        print("Please select an existing statistical function")
# =============================================================================
# #[3]rd selection - Generating plot
# =============================================================================
        elif user_input == 3:
            if not data_loaded:
                print()
                print('+'+'-'*40+'+\n'+
                      '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
                      '|' + ' '*3 + 'Please load data before continuing' + ' '*3 + '|\n'+
                      '+' + '-'*40 + '+') #if not, print
            else:
                pass
        if user_input == 4:
            print()
            print('The program has been terminated')
            break
                
            
                