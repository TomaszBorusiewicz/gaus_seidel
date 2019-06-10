import numpy as np
from scipy.optimize import minimize, fmin_powell
import matplotlib.pyplot as plt


def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1*x2 * (x3 * x4)


n = 4
x0 = np.zeros(n)
x0[0] = 1.0
x0[1] = 4.0
x0[2] = 5.0
x0[3] = 2.0
b = (1.0, 5.0)
bnds = (b, b, b, b)
solution = minimize(objective, x0, method='SLSQP', bounds=bnds)
print(solution)

# minimize_func = minimize(objective, x0, method="Nelder-Mead")
# print(minimize_func)
# plt.plot(linear[0], linear[1])
# plt.show()
