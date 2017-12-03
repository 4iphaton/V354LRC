import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
import math

A, t = np.genfromtxt('../../content/values/',unpack=True)

print(A, t)

t *= 1e-6

def f(x, b):
    return np.exp(-x) + b
   # return x*b**2-b**3*y

parameters, pcov = curve_fit(f, A, t)
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')
t= np.linspace(0,80000,1000)

plt.plot(t, f(t, *parameters), 'g-', label='Fit')
plt.savefig('build/plot1.pdf')
