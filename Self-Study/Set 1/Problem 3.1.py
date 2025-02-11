import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# y'' + 2y' + 2y = 1

def fun(t, y):
    ddt = np.zeros(2)

    ddt[0] = y[1]
    ddt[1] = 1 - 2*y[1] -2*y[0]

    return ddt

solution = solve_ivp(fun, [0,10], [2,-3/2], t_eval=np.linspace(0,10,100))   



plt.plot(solution.t, solution.y[0], label='y(t)')
#Exact
x = np.linspace(0,10,100)   
y = 3/2 * np.cos(x) * np.exp(-x) + 1/2
plt.plot(x, y, label='Exact')

plt.legend()
plt.show()