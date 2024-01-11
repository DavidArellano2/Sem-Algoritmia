"""
@author: David_Lopez
"""
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

def f(x):
    y = x**5 + 8*x**2 - 5*x + 2
    return y
def f_primera_derivada(x):
    return 5*x**4 + 16*x - 5
def f_segunda_derivada(x):
    return 20*x**3 + 16

t = np.arange(-2,2,0.001)

plt.figure()
plt.title(" GRAFICAS, TAREA 1",
          #position = (0.75, 0.85),
          fontsize = 18,
          color = "Red",
          fontweight = "bold")
plt.plot(t, f(t), label='f(x)')
plt.plot(t, f_primera_derivada(t), label="f'(x)")
plt.plot(t, f_segunda_derivada(t), label="f''(x)")
plt.show()