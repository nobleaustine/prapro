import pytest
import numpy as np
import multiprocessing.shared_memory as sm
from task_11 import process_pool, multi_process

inputs = [
    [10000, 5, 2000],
    [10000000, 10, 1000000],
    [1000000, 20, 50000],
]


@pytest.mark.parametrize("input", inputs)
def test_process(input):
    memory = sm.SharedMemory(create=True, name="memory", size=16 * input[0])
    array = np.ndarray((input[0],), buffer=memory.buf, dtype=int)
    multi_process(input[0], input[2])

    assert len(array) == input[0]

    memory.close()
    memory.unlink()


@pytest.mark.parametrize("input", inputs)
def test_process_pool(input):
    memory = sm.SharedMemory(create=True, name="memory", size=16 * input[0])
    array = np.ndarray((input[0],), buffer=memory.buf, dtype=int)
    process_pool(input[0], input[1], input[2])

    assert len(array) == input[0]

    memory.close()
    memory.unlink()
