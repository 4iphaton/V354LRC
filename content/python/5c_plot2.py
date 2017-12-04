import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

L = ufloat(10.11 , 0.03)*(10 **(-3))
C = ufloat(2.098, 0.006) *(10 **(-9))
R_1 = ufloat(48.1, 0.1)
R_2 = ufloat(509.5, 0.5)
R_g = 50

U , nu = np.genfromtxt('content/values/kondensatorspannung_val.txt',unpack=True)

nu *= 1000
U = U/10

print( "U_c", U, "nu", nu)



U_max = 39
q_e = U_max/10
q_t = (1/(R_2+R_g))*(unp.sqrt(L/C))
#w_0 = 34000
#w_res = unp.sqrt((1/(L*C))-((R_2+R_g)**2/(2*(L)**2)))
b_t = (R_2+R_g)/L

print("t", q_t, "e", q_e, b_t )#"res", w_res )
#abs. 1
Ua = (1/unp.sqrt(2))*(U_max/10)

plt.plot(nu ,U ,'r-' ,label='Messwerte' )
plt.xlim(27500, 40000, 14)
plt.ylim(2, 4)
plt.grid()
#def konst(x):
#    return Ua * (x/x)

plt.axhline(Ua)
plt.axvline(28900)
plt.axvline(38300)

plt.xlabel(r'$nu/[1/s]$')
plt.ylabel(r'$U_c/U$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot3.pdf')
print('------------------')
