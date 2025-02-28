# library imports
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from ipywidgets import interact, interact_manual, FloatSlider, fixed
import sympy as sp


# Transfer function

## 4s^2 + 3s + 2 / s^3 + 2s^2 - 6s + 5

numerator = [4, 3, 2]
denominator = [1, 2, -6, 5]

zeros = np.roots(numerator)
poles = np.roots(denominator)

print("Zeros:", zeros)
print("Poles:", poles)

real_parts_zeros = np.real(zeros)
imag_parts_zeros = np.imag(zeros)
real_parts_poles = np.real(poles)
imag_parts_poles = np.imag(poles)

# Plot
plt.plot(real_parts_zeros, imag_parts_zeros, 'o', label='Zeros')
plt.plot(real_parts_poles, imag_parts_poles, 'x', label='Poles')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.show()