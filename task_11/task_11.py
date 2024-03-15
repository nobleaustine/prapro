# Task 11

# Use multiprocessing to fill random values in a large numpy array.

# References:
# multiprocessing.shared_memory.SharedMemory
# concurrent.futures.ProcessPoolExecutor

# Read about:
# Python Global Interpreter Lock (GIL)
# Multiprocessing start methods: spawn, fork, forkserver

import numpy as np
import multiprocessing as mp
import multiprocessing.shared_memory as sm
from concurrent.futures import ProcessPoolExecutor


# function to fill array
def fill_array(part):
    np.random.seed()
    s = part.start
    e = part.stop
    l = e - s
    array[s:e] = np.random.randint(0, 100, size=l, dtype=np.int16)


# function use a pool to fill random numbers
def process_pool(n, p, chunk_size):
    with ProcessPoolExecutor(max_workers=p) as executor:
        futures = []
        for i in range(0, n, chunk_size):
            futures.append(executor.submit(fill_array, slice(i, i + chunk_size)))


# function to use simple process
def multi_process(n, chunk_size):
    futures = []
    for i in range(0, n, chunk_size):
        p = mp.Process(target=fill_array, args=[slice(i, i + chunk_size - 1)])
        p.start()
        futures.append(p)

    for p in futures:
        p.join()


if __name__ == "__main__":
    # taking array size and process number from user
    n = int(input("Enter the size of the array: "))
    p = int(input("Enter the number of processes: "))

    # size each process should fill
    chunk_size = n // p

    # creating array that all process can access
    memory = sm.SharedMemory(create=True, name="memory", size=16 * n)
    array = np.ndarray((n,), buffer=memory.buf, dtype=int)

    process_pool(n, p, chunk_size)

    print(array)

    memory.close()
    memory.unlink()
