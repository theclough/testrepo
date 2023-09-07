# 3.2

import numpy as np
import matplotlib.pyplot as plt

def newQ():
    print('----------------')

# 1)

x = np.linspace(1,100,100)
y = np.arange(1,101,1,dtype=int)

# check lengths the same

print(len(x) == len(y))

newQ()

# 2)

print(x[0:3])

newQ()

# 3)

print('The first 3 entires of x are:', x[0], ',', end=' ')
print(x[1], ', and ', x[2])

newQ()

# 4)

w = 10**(-np.linspace(1,10,10))
x = np.arange(-10, -110, -10, dtype=int)

plt.figure()
plt.semilogy(x,w)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 5)

s = 3*w

plt.figure()
plt.semilogy(x,w)
plt.semilogy(x,s)
plt.xlabel('x')
plt.savefig('Lab1_3-2_Figure.png')