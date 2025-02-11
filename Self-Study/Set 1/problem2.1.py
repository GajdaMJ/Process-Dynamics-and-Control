import sympy
import numpy as np
import matplotlib.pyplot as plt
from sympy import Function, dsolve, Derivative, symbols
# y'' + 5y' + 4y = 2
t = symbols('t')
y = Function('y')(t)

yp = Derivative(y, t)
ypp = Derivative(y, t, t)

# Define the differential equation
ode = ypp + 5*yp + 4*y - 2

# Solve the differential equation with initial conditions
result = dsolve(ode, y, ics={y.subs(t, 0): 0, yp.subs(t, 0): 1})

print(result)