import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math

phi, nu = np.genfromtxt('../../content/values/phase_val.txt', unpack=True)

phi *= 2*const.pi/20

phi = np.log(phi)

plt.plot(nu, phi, 'kx', label='Phase logarithmisch')
plt.xlabel(r'$\omega [kHz]$')
plt.ylabel(r'$\phi / rad$')
plt.legend(loc='best')
plt.tight_layout()
#plt.savefig('build/pendel.pdf')
plt.show()
