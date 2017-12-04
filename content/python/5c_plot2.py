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

U_c , nu = np.genfromtxt('content/values/kondensatorspannung_val.txt',unpack=True)

nu *= 1000
U_c = U_c/10

print( "U_c", U_c, "nu", nu)
U_c_log = np.log(U_c)


U_max = 39
q_e = U_max/10
q_t = (1/(R_2+R_g))*(unp.sqrt(L/C))
#w_0 = 34000
#w_res = unp.sqrt((1/(L*C))-((R_2+R_g)**2/(2*(L)**2)))
b_t = (R_2+R_g)/L

print("t", q_t, "e", q_e, b_t )#"res", w_res )
#abs. 1
u_b = ((1/np.sqrt(2))*(U_max)/10

plt.plot(nu ,U_c ,'r-' ,label='Messwerte' )
plt.xlimit(25000, 45000)
plt.grid()


plt.axhline(u_b)
#plt.axvline

plt.xlabel(r'$nu/[1/s]$')
plt.ylabel(r'$U_c/U$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot3.pdf')
print('-----------------')
