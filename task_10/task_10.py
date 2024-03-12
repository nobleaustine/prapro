# Task 10

# Implement gradient descent in python on the data:
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Plot the fit after every few iterations.

# References:
# matplotlib

import visdom
import numpy as np
import matplotlib.pyplot as plt

# function to plot actual and predicted line
def plot_graph(m, c):

    global x,window

    p = m * x + c
    y = 2 * x

    viz.line(
        X=x,
        Y=np.column_stack((y, p)),
        win=window,
        update='replace',
        opts=dict(
            legend=["actual", "predicted"],
            xlabel='x',
            ylabel='y',
            title="Gradient Descent Algorithm (UPDATE) ", 
            linecolor=np.array([[0, 255, 0],[225, 0, 0]])
                )
        )

    viz.line(
        X=x,
        Y=np.column_stack((y, p)),
        opts=dict(
            legend=["actual", "predicted"],
            xlabel='x',
            ylabel='y',
            title="Gradient Descent Algorithm", 
            linecolor=np.array([[0, 255, 0],[225, 0, 0]])
                )
        )
    
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

        if __name__ == "__main__":
            if i % 100 == 0:
                plot_graph(w[0][0], b[0][0])

    return w[0][0], b[0][0]

if __name__ == "__main__":

    # data visualization tool
    viz = visdom.Visdom(server='http://localhost', port=8097)
    assert viz.check_connection(), "connection failed: check if Visdom server is running."

    # data
    X = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    Y = np.array([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]])
    X = X.T
    Y = Y.T

    window = viz.line(
        X=x,
        Y=np.column_stack((2*x, np.random.rand(10))),
        opts=dict(
            legend=["actual", "predicted"],
            xlabel='x',
            ylabel='y',
            title="Gradient Descent Algorithm (UPDATE)", 
            linecolor=np.array([[0, 255, 0],[225, 0, 0]])),
            )

    # GDA on action
    w, b = GDA(X, Y, 100000)
    print("slope: ", round(w, 6), " intercept: ", round(b, 6))
    
    viz.close()
