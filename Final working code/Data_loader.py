import re #In case if we would like to make some changes in Nx, Ny, Nz inputs
from Function_file import dataLoad

def dataLoader():
    while True:
        try:
            user_input = input('┏' + '━'*39 + '┓\n'+
                             '┃'+' '*5+'You are now in Load data menu'+' '*5+'┃\n'+
                             '┃Please insert file name and upload file┃\n'+
                             '┃'+' '*2+'Or type "q" to return to main menu'+' '*3+'┃\n'+
                             '┗' + '━'*39 + '┛\n>>')
            if user_input.lower()=='q':
                return None
            elif not user_input.endswith('.bin'):
                
                # Calculating the length of the user_input string
                input_length = len(user_input)
                
                # Calculating the number of dashes needed for the top and bottom borders
                num_dashes = input_length + 26
                
                # Constructing the message with adjusted borders
                message=('+' + '-' * (num_dashes+7) + '+\n'
                        f'| {" " * ((num_dashes - input_length - 24) // 2)}{user_input} needs to have .bin extension{" " * ((num_dashes - input_length - 24) // 2)} |\n'+
                        f'| {" " * ((num_dashes - input_length - 24) // 2 + 2)}Error loading data from {user_input}{" " * ((num_dashes - input_length - 24) // 2 + 3)} |\n'+
                        f'| {" " * ((num_dashes - input_length - 24) // 2 + 9)}Please try again☺{" " * ((num_dashes - input_length - 24) // 2 + 9)}|\n'+
                        '+' + '-' * (num_dashes+7) + '+')
                
                #Printing the message
                print(message)
                return None
            
            filename=user_input
            
#=============================================================================
#[1] Main input option. User enters dimesions him/herselfe
#=============================================================================            
            # while True:

            #     print('┏' + '━'*49 + '┓\n'+
            #           '┃Enter the dimensions of the 3D array (Nx, Ny, Nz)┃\n'+
            #           '┃' + ' '*7 +'Or type "q" to return to main menu'+ ' '*8 + '┃\n'+
            #           '┗' + '━'*49 + '┛\n')
                
            #     Nx=input('Nx:').strip()
            #     if Nx.lower()=='q':
            #         return None
            #     elif Nx.isdigit():
            #         Nx=int(Nx)
            #     else:
            #         print('+'+'-'*40+'+\n'+
            #               '|' + ' '*9 + 'WARNING! Invalid input.' + ' '*8 + '|\n'+
            #               '|' + ' '*4 + ' Please enter a positive integer' + ' '*4 + '|\n'+
            #               '|Or type "q" to return to the main menu. |\n'+
            #               '+' + '-'*40 + '+')
            #         continue
                
            #     Ny=input('Ny: ').strip()
            #     if Ny.lower() == 'q':
            #         return None
            #     elif Ny.isdigit():
            #         Ny=int(Ny)
            #     else:
            #         print('+'+'-'*40+'+\n'+
            #               '|' + ' '*9 + 'WARNING! Invalid input.' + ' '*8 + '|\n'+
            #               '|' + ' '*4 + ' Please enter a positive integer' + ' '*4 + '|\n'+
            #               '|Or type "q" to return to the main menu. |\n'+
            #               '+' + '-'*40 + '+') 
            #         continue
                
            #     Nz=input('Nz: ').strip()
            #     if Nz.lower() == 'q':
            #         return None
            #     elif Nz.isdigit():
            #         Nz=int(Nz)
            #         break
            #     else:
            #         print('+'+'-'*40+'+\n'+
            #               '|' + ' '*9 + 'WARNING! Invalid input.' + ' '*8 + '|\n'+
            #               '|' + ' '*4 + ' Please enter a positive integer' + ' '*4 + '|\n'+
            #               '|Or type "q" to return to the main menu. |\n'+
            #               '+' + '-'*40 + '+')
            #         continue
#=============================================================================
#[2]nd possible option. Creating selection options of Nx x Ny x Nz (This part additional)
#=============================================================================
              
            size=['32 x 32 x 8192','16 x 32 x 16384','8 x 16 x 65536'] # there are plenty of possibilities for input       
            while True:
                print('┏' + '━'*45 + '┓\n'+
                      '┃Enter the dimensions of the 3D array (Nx, Ny, Nz)┃\n'+
                      '┃' + ' '*5 +'Or type "q" to return to main menu'+ ' '*6 + '┃\n'+
                      '┗' + '━'*45 + '┛\n')
                
                Nx=input('Nx: ').strip()
                if Nx.lower()=='q':
                    return None
                elif Nx.isdigit():
                    Nx=int(Nx)
                else:
                    print('Invalid input. Please enter a positive integer or type "quit" to return to the main menu.')
                    continue
                
                Ny=input('Ny: ').strip()
                if Ny.lower() == 'q':
                    return None
                elif Ny.isdigit():
                    Ny=int(Ny)
                else:
                    print('Invalid input. Please enter a positive integer or type "quit" to return to the main menu.') 
                    continue
                
                Nz=input('Nz: ').strip()
                if Nz.lower() == 'q':
                    return None
                elif Nz.isdigit():
                    Nz=int(Nz)
                user_input_size=int(input('┏' + '━'*68 + '┓\n'+
                                          '┃Please select which size of 3D array you want to create (Nx x Ny Nz)┃\n'+
                                          '┗' + '━'*68 + '┛\n'+
                                          "[1] 32 x 32 x 8192\n" +
                                          "[2] 16 x 32 x 16384\n" +
                                          "[3] 8 x 16 x 65536\n"  +
                                          "[4] 128 x 128 x 512\n"+
                                          "[5] 256 x 256 x 128\n"+
                                          "[6] Return to Load Menu\n"+
                                          ">>"))
                if user_input_size == 1:
                    Nx, Ny, Nz=[int(val) for val in size[user_input_size-1].split(' x ')]
                    break
                    
                elif user_input_size == 2:
                    Nx, Ny, Nz=[int(val) for val in size[user_input_size-1].split(' x ')]
                    break
                    
                elif user_input_size == 3:
                    Nx, Ny, Nz=[int(val) for val in size[user_input_size-1].split(' x ')]
                    break
                    
                elif user_input_size == 4:
                    Nx, Ny, Nz=[int(val) for val in size[user_input_size-1].split(' x ')]
                    break
                    
                elif user_input_size == 5:
                    Nx, Ny, Nz=[int(val) for val in size[user_input_size-1].split(' x ')]
                    break 
                    
                elif user_input_size == 6:
                    return None
                    break
                    
                else:
                    print("Invalid input. Please select a valid option.")
                    continue
               
            matrix_3d = dataLoad(filename, Nx, Ny, Nz)
            
            if matrix_3d is not None:
                # File loaded successfully, so break out of the while loop
                break
            else:
                # File not loaded successfully, so continue the while loop
                continue
            
        except:
            
            # Calculating the length of the filename string
            filename_length = len(filename)
            
            # Calculating the number of dashes needed for the top and bottom borders
            num_dashes = filename_length + 28
            
            # Constructing the message with adjusted borders
            message = ('+' + '-' * num_dashes + '+\n'
                       f'| {" " * ((num_dashes - filename_length - 26) // 2)}Error loading data from {filename}.{" " * ((num_dashes - filename_length - 27) // 2)} |\n'+
                       f'| {" " * ((num_dashes - filename_length - 26) // 2 + 8)}Please try again{" " * ((num_dashes - filename_length - 27) // 2 + 7)} |\n'+
                       '+' + '-' * num_dashes + '+')
            
            #Printing the message
            print(message)
        
    return matrix_3d