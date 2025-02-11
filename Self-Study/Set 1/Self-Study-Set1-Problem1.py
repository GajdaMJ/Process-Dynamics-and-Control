#(2+3i)(3+2i)
import numpy as np
print((2+3j)*(3+2j))

print((2+4j)/(1+1j))

print(np.cos(-2*np.pi/3) + 1j*np.sin(-2*np.pi/3))

print(f"magnitude of 4-2i is {np.sqrt(4**2 + (-2**2))} and argument is {np.angle(4-2j)}")

print(f'magnitude of (2+3i)/(4+5i) is {np.absolute((2+3j)/(4+5j))} and argument is {np.angle((2+3j)/(4+5j))}')

# (1+i)^2011

print((1+1j)**2011)