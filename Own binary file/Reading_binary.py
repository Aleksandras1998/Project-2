import numpy as np
from Creating_binary import data

filename='small 3D array.bin'
# Read the binary file back into a 3D array
with open(filename, "rb") as file:
    binary_data = file.read()
array_from_file = np.frombuffer(binary_data, dtype=data.dtype).reshape(data.shape)
print(np.round(array_from_file,4))
# for i in range(array_from_file.shape[0]):
#     print(array_from_file[i,:,:])

#print(array_from_file[0,:,0])