import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, exp

# y'''' + y''' -3y'' -5y' - 2y = 0

poly = [1,1,-3,-5,-2]

roots = np.roots(poly)

print(roots)

#y(0) = 0, y'(0) = 5, y''(0) = 1, y'''(0) = 9

t = symbols('t')    
c1, c2, c3, c4 = symbols('c1 c2 c3 c4')
yt = c1*exp(roots[0]*t) + c2*exp(roots[1]*t) + c3*exp(roots[2]*t) + c4*exp(roots[3]*t)

print(yt)

yt_prime = yt.diff(t)
yt_pprime = yt_prime.diff(t)
yt_ppprime = yt_pprime.diff(t)

eq1 = Eq(yt.subs(t,0), 0)
eq2 = Eq(yt_prime.subs(t, 0), 5)
eq3 = Eq(yt_pprime.subs(t, 0), 1)
eq4 = Eq(yt_ppprime.subs(t, 0), 9)

constants = solve((eq1, eq2, eq3, eq4), (c1, c2, c3, c4))

print(constants)


yt = yt.subs(constants)
print("Particular solution of the differential equation:")
print(yt)