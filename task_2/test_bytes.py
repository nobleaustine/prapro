from task_2 import random_array, bytes_array, recreated_array, elapsed_time
import numpy as np


# test if time is a float object
def test_time():
    assert isinstance(elapsed_time, float)


# checking if actual and recreated array are same
def test_same():
    assert random_array.all() == recreated_array.all()


# testing if dimension is 1000x1000
def test_shape():
    assert random_array.shape == (1000, 1000)
    assert random_array.shape == recreated_array.shape


# testing data types
def test_type():
    assert random_array.dtype == np.float64
    assert recreated_array.dtype == np.float64
    assert isinstance(bytes_array, bytes) == True
