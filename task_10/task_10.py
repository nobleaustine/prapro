# Task 10

# Implement gradient descent in python on the data:
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Plot the fit after every few iterations.

# References:
# matplotlib

import numpy as np
import matplotlib.pyplot as plt


# function to plot actual and predicted line
def plot_graph(m, c):

    global x
    p = m * x + c
    y = 2 * x

    plt.plot(x, y, label="Actual Line", color="green")
    plt.plot(x, p, label="Predicted Line", color="red")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Gradient Decent Algorithm: Slope={round(m,3)}, Intercept={round(c,3)}")
    plt.legend()
    plt.show()


# function to perform GDA
def GDA(X, Y, epochs):

    # initializing random weight and bias
    w = np.random.rand(1, 1)
    b = np.random.rand(1, 1)
    n = len(X)
    B = np.full((n, 1), b)
    I = np.ones((n, 1))

    for i in range(epochs):

        print("epoch: ", i)
        P = X @ w + I @ b

        # loss = 1/2(P-Y)^2
        dL_dP = P - Y
        dP_dw = X.T
        dP_db = I.T

        # gradient
        dL_dw = dP_dw @ dL_dP
        dL_db = dP_db @ dL_dP

        # update
        w = w - 0.001 * dL_dw
        b = b - 0.001 * dL_db

        # returning if w,b is infinity
        if abs(w[0][0]) == float("inf") or abs(b[0][0]) == float("inf"):
            return w[0][0], b[0][0]

        if __name__ == "__main__":
            if i % 100 == 0:
                plot_graph(w[0][0], b[0][0])

    return w[0][0], b[0][0]


if __name__ == "__main__":
    # data
    X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Y = np.array([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]])
    X = X.T
    Y = Y.T

    # GDA on action
    w, b = GDA(X, Y, 1000)
    print("slope: ", round(w, 6), " intercept: ", round(b, 6))
