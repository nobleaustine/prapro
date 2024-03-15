import subprocess
import pytest

l1 = [[2, 3, 5], [-1, 3, -2], [3.2, -1.2, 2]]


@pytest.mark.parametrize("n", l1)
def test_add(n):
    a = str(float(n[0]))
    b = str(float(n[1]))
    c = str(float(n[0]) + float(n[1]))
    result = subprocess.run(["python", "task_12.py", a, b], stdout=subprocess.PIPE)
    output = result.stdout.decode().strip()
    output = output.split("\n")[1]
    assert output == f"{a} + {b} = {c}"


@pytest.mark.parametrize("n", l1)
def test_multiply(n):
    a = str(float(n[0]))
    b = str(float(n[1]))
    c = str(float(n[0]) * float(n[1]))
    result = subprocess.run(
        ["python", "task_12.py", a, b, "-m"], stdout=subprocess.PIPE
    )
    output = result.stdout.decode().strip()
    output = output.split("\n")[1]
    assert output == f"{a} x {b} = {c}"
