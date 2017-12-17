import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

t1, A1 = np.genfromtxt('content/values/Amplituden_max_val.txt',unpack=True)
t2, A2 = np.genfromtxt('content/values/Amplituden_min_val.txt',unpack=True)
t, A = np.genfromtxt('content/values/Amplituden_val.txt',unpack=True)

A2 = -A2

print(A, t)

t/=1000000
t1/=1000000
t2/=1000000

def f(x, a,b):
    return np.exp(x*a+b)
   # return x*b**2-b**3*y

parameters, pcov = curve_fit(f, t, A)
errors = np.sqrt(np.diag(pcov))
print(parameters, errors, sep='\n')
ln = np.linspace(t[0],t[len(t)-1],5000)

plt.plot(ln, f(ln, *parameters), 'g-', label='Fit')
plt.plot(t1,A1,'rx',label='Maxima')
plt.plot(t2,A2,'bx',label='Minima')
plt.xlabel(r'$t [s]$')
plt.ylabel(r'$U [V]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')
print('----------------')
