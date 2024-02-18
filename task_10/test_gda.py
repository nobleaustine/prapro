from task_10 import GDA
import pytest
import numpy as np


@pytest.fixture
def give_x():
    X = np.random.rand(3, 10, 1)
    return X


@pytest.fixture
def give_y():
    Y = np.random.rand(3, 10, 1)
    return Y


def test_gda(give_x, give_y):

    for x, y in zip(give_x, give_y):
        w, b = GDA(x, y, 1000)
        assert abs(w) != float("inf") and abs(b) != float("inf")
