import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

U_c , nu = np.genfromtxt('content/values/Amplituden_val.txt',unpack=True)


print( "U_c", U_c, "nu", nu)

def f(x, a, b):
   return a*x + b

#abs. 1

parameters, pcov = curve_fit(f, U_c, nu)
errors = np.sqrt(np.diag(pcov))
print(parameters, errors, sep='\n')
ln = np.linspace(nu[0],nu[len(nu)-1],5000)

plt.plot(ln, f(ln, *parameters), 'g-', label='Fit')
plt.plot(nu , U_c ,'rx',label='Messwerte')
plt.xlabel(r'$nu/[s]$')
plt.ylabel(r'$U_c/[V]$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
print('----------------')
