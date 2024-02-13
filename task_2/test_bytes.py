from task_2 import random_array,bytes_array,recreated_array,elapsed_time
import numpy as np

def test_time():
    assert isinstance(elapsed_time,float) 

def test_same():
    assert random_array.all() == recreated_array.all()

def test_shape():
    assert random_array.shape == (1000,1000)
    assert random_array.shape == recreated_array.shape

def test_type():
    assert random_array.dtype == np.float64
    assert recreated_array.dtype == np.float64
    assert isinstance(bytes_array,bytes) == True