import numpy as np
import matplotlib.pyplot as plt

# y'''' + y''' -3y'' -5y' - 2y = 0

poly = [1, 1, -3, -5, -2]

roots = np.roots(poly)

print("Roots of the characteristic equation:", roots)

# General solution
# yt = c1*exp(r1*t) + c2*exp(r2*t) + c3*exp(r3*t) + c4*exp(r4*t)
# where r1, r2, r3, r4 are the roots of the characteristic equation

general_solution = "yt = "
for i, root in enumerate(roots):
    general_solution += f"c{i+1}*exp({root}*t) + "

# Remove the last ' + '
general_solution = general_solution[:-3]

print("General solution of the differential equation:")
print(general_solution)

# Initial conditions
# y(0) = 0, y'(0) = 5, y''(0) = 1, y'''(0) = 9