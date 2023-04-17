import re #In case if we would like to make some changes in Nx, Ny, Nz inputs
from Function_file import dataLoad

def dataLoader():
    while True:
        try:
            user_input = input('┏' + '━'*41 + '┓\n'+
                             '┃You are in the Load data menu┃\n'+
                             '┃Please insert file name and upload file ┃\n'+
                             '┃Or type "q" to return to main menu┃\n'+
                             '┗' + '━'*41 + '┛\n>>')
            if user_input.lower()=='q':
                return None
            elif not user_input.endswith('.bin'):
                print('+'+'-'*34+'+\n'+
                      f'| {" " * 0}{user_input} needs to have .bin extension{" " * 0} |\n'+
                      f'| {" " * 2}Error loading data from {user_input}{" " * 3} |\n'+
                      '|' + ' '*9 + 'Please try again' + ' '*9 + '|\n'+
                      '+'+'-'*34+'+')
                return None
            
            filename=user_input
            
            while True:
                print('┏' + '━'*41 + '┓\n'+
                      '┃ Enter the dimensions of the data (Nx, Ny, Nz): ┃\n'+
                      '┃Or type "q" to return to main menu┃'
                      '┗' + '━'*41 + '┛\n>>')
                
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
            print(f'Error loading data from {filename}. Please try again')
        
    return matrix_3d