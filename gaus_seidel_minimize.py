import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from gauss_seidell import gaus_seidel


def objective(x):
    return np.sin(x)


x0 = np.array([10])  # initial guess
solve = minimize(objective, x0, method=gaus_seidel)
x_min = solve.x
print(solve)

# plot your function to visualize the outcome
x_func = np.linspace(1, 100, 1000)
y_func = []
for item in x_func:
    y_func.append((objective(np.asarray([item]))))

y_min = objective(np.asarray([x_min]))

plt.plot(x_func, y_func)
plt.plot(x_min, y_min, "ro")
plt.show()
