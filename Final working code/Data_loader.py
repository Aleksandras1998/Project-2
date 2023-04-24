import re #In case if we would like to make some changes in Nx, Ny, Nz inputs
from Function_file import dataLoad

def dataLoader():
    while True:
        try:
            user_input = input('┏' + '━'*39 + '┓\n'+
                             '┃'+' '*4+'You are now in Load data menu'+' '*5+'┃\n'+
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
            
            while True:
                print('┏' + '━'*45 + '┓\n'+
                      '┃Enter the dimensions of the 3D array (Nx, Ny, Nz)┃\n'+
                      '┃' + ' '*5 +'Or type "q" to return to main menu'+ ' '*6 + '┃\n'+
                      '┗' + '━'*45 + '┛\n')
                
                Nx=input('Nx:').strip()
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
                    break
                else:
                   print('Invalid input. Please enter a positive integer or type "quit" to return to the main menu.')
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