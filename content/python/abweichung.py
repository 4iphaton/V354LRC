import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math
from uncertainties import unumpy as unp

L = ufloat(10.11 , 0.03)*(10 **(-3))
C = ufloat(2.098, 0.006) *(10 **(-9))
R_1 = ufloat(48.1, 0.1)
R_2 = ufloat(509.5, 0.5)
R_g = 50

a_a1= ((48.1 - 535 )/48.1)*100
a_a2= ((509.5 - 535 )/509.5)*100
b_1= ((4390 - 3400 )/4390)*100
c_1=((3.923 -3.9)/3.923)*100
c_2=((8808 - 9400)/8808)*100

print(a_a1, "     ", a_a2, "     ", b_1, "c", c_1, "      ", c_2)


#murks
w_r1 = (1/2*const.pi)*unp.sqrt((1/(L*C))-(((R_1)**2)/(2*(L)**2)))
w_r2 =(1/(unp.sqrt(L*C)))*(1/(2*const.pi))
print(w_r1,"      ", w_r2)
