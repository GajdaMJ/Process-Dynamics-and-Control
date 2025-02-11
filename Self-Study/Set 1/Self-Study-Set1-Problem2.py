import numpy as np
import matplotlib.pyplot as plt
# y'' + 5y' + 4y = 2

poly = [1, 5, 4]

print(np.roots(poly))

#yt = c1*exp(-t) + c2*exp(-4t) + 1/2
# y(0) = 0 ; y'(0)=1
# 
# c1 + c2 + 1/2 = 0
# -c1 -4c2 = 1

a=np.array([[1,1],[-1,-4]])
b=np.array([-1/2,1])

print(np.linalg.solve(a,b)) 
x= np.linalg.solve(a,b)
print(f'y(t) = {x[0]}*exp(-t) + {x[1]}*exp(-4t) + 1/2')


 