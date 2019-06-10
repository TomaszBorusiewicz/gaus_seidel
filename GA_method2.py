import gauss_seidell as ga
import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return sum([np.sin(t) for t in x])


params = {
        "x1": ["real", (-512, 512)],
        "x2": ["real", (-512, 512)],
    }
nm = ga.gaus_seidel(func, params)
nm.minimize(n_iter=30)
print(nm.p_max)
plt.plot(nm.p_max, nm.p_min)
plt.show()
