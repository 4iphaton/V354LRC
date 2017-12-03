import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

t, A = np.genfromtxt('content/values/Amplituden_max_val.txt',unpack=True)


print(A, t)

t/=1000000

def f(x, a,b):
    return np.exp(x*a+b)
   # return x*b**2-b**3*y

parameters, pcov = curve_fit(f, t, A)
errors = np.sqrt(np.diag(pcov))
print(parameters, errors, sep='\n')
ln = np.linspace(t[0],t[len(t)-1],5000)

plt.plot(ln, f(ln, *parameters), 'g-', label='Fit')
plt.plot(t,A,'gx',label='Values')
plt.savefig('build/plot1.pdf')
print('----------------')
