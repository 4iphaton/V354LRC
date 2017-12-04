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

print( "U_c", U_c, "nu", nu)
U_c_log = np.log(U_c)


U_max = 39
q_e = U_max/10
q_t = (1/(R_2+R_g))*unp.sqrt(L/C)
#w_0 = 34000
#w_res = unp.sqrt((1/(L*C))-((R_2+R_g)**2/(2*(L)**2)))


print("t", q_t, "e", q_e, )#"res", w_res )
#abs. 1
U_b = np.log((1/np.sqrt(2))*U_max)

#b_e= w_0/q_e
b_t = (R_2+R_g)/L
#a_b= (w_res-w_0)/w_res
#print("breite", b_e, "theo", b_t, "ab", a_b)
#parameters, pcov = curve_fit(f, U_c, nu)
#errors = np.sqrt(np.diag(pcov))
#print(parameters, errors, sep='\n')
#ln = np.linspace(nu[0],nu[len(nu)-1], 4)

#plt.plot(ln, f(ln, *parameters), 'g-', label='Fit')
plt.plot(nu , U_c_log ,'bx',label='Messwerte')


#plt.axhline(U_b)
#plt.axvline
#plt.plot(nup , 'rb', label='nup')
#plt.xscale('log')
#plt.yscale('log')

plt.xlabel(r'$nu/[1/s]$')
plt.ylabel(r'$log(U_c/U)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
print('----------------')

plt.plot(nu , U_c_log ,'bx',label='Messwerte')


plt.axhline(U_b, 'r--')
#plt.axvline
#plt.plot(nup , 'rb', label='nup')
#plt.xscale('log')
#plt.yscale('log')

plt.xlabel(r'$nu/[1/s]$')
plt.ylabel(r'$log(U_c/U)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')
print('----------------')
