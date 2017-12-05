import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math

phi, nu = np.genfromtxt('content/values/phase_val.txt', unpack=True)

phi *= 2*const.pi/20

plt.plot(nu, phi, 'kx', label='Phase linear')
plt.grid(15)
#plt.axhline(const.pi/np.sqrt(2))
plt.axhline(const.pi/4)
plt.axhline(3*const.pi/4)
plt.axhline(const.pi/2)
plt.axvline(32)
plt.axvline(25)
plt.axvline(34.55)
plt.xlabel(r'$\nu / [kHz]$')
plt.ylabel(r'$\phi / rad$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot4.pdf')
print('-------------------')


#plt.savefig('build/pendel.pdf')
plt.show()
L = ufloat(10.11 , 0.03)*(10 **(-3))
C = ufloat(2.098, 0.006) *(10 **(-9))
R_1 = ufloat(48.1, 0.1)
R_2 = ufloat(509.5, 0.5)
R_g = 50#
w1= (-(R_g+R_2)/(2*L)+(((R_g+R_2)/(2*L))**2+1/(L*C))**(1/2))/(2*const.pi)
print('Theoretische Werte')
print('w1=',(-(R_g+R_2)/(2*L)+(((R_g+R_2)/(2*L))**2+1/(L*C))**(1/2))/(2*const.pi))
print('w2=',((R_g+R_2)/(2*L)+(((R_g+R_2)/(2*L))**2+1/(L*C))**(1/2))/(2*const.pi))
print('wres=',((R_g+R_2)/L/(2*const.pi))/2+w1)
print('Praktische Werte /e3')
print('w1=',25)
print('w1=',34.55)
print('wres=',34.55-25)
