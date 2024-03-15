from task_10 import GDA
import pytest
import numpy as np


@pytest.fixture
def give_x():
    X = np.random.rand(3, 10, 1)
    return X


@pytest.fixture
def give_y(give_x):
    Y = []
    for x in give_x:
        Y.append((x * 2) + 3)
    Y = np.array(Y)
    return Y


def test_gda(give_x, give_y):
    for x, y in zip(give_x, give_y):
        slope, intercept = np.polyfit(np.ravel(x), np.ravel(y), 1)
        w, b = GDA(x, y, 10000)
        assert np.isclose(slope, w, atol=0.1) == True
        assert np.isclose(intercept, b, atol=0.1) == True
