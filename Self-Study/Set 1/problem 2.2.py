import sympy
import numpy as np
import matplotlib.pyplot as plt
from sympy import Function, dsolve, Derivative, symbols
# y'''' + y''' -3y'' -5y' - 2y = 0


t = symbols('t')
y = Function('y')(t)

yp = Derivative(y, t)
ypp = Derivative(y, t, t)
yppp = Derivative(y, t, t, t)
ypppp = Derivative(y, t, t, t, t)

# Define the differential equation
ode = ypppp + yppp - 3*ypp - 5*yp - 2*y

result = dsolve(ode, y, ics={y.subs(t, 0): 0, yp.subs(t, 0): 5, ypp.subs(t, 0): 1, yppp.subs(t, 0): 9})

print(result)