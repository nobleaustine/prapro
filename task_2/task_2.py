# Create a 1000 x 1000 random numpy array
# Measure how long the creation takes
# Convert the array into bytes
# Recreate the array from the bytes

# References:
# time package
# numpy package
# np.frombuffer

import numpy as np
import time

# creating a random array and measuring time taken for creation
start = time.time()
random_array = np.random.rand(1000,1000)
end = time.time()
elapsed_time = end - start
print("Elapsed time    : ",elapsed_time)

# converting to bytes and converting back
print("random_array    : ",random_array[0][0:6])
bytes_array = random_array.tobytes()
print("bytes_array     : ",bytes_array[0:6])
# adding datatype(float64) and shape(1000,1000) of random array
recreated_array = np.frombuffer(bytes_array,dtype=np.float64).reshape(1000,1000)
print("recreated_array : ",recreated_array[0][0:6])