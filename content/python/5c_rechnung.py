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

U_0 = 15
U_m = 39

#U_c
q_t = (1/(R_1+50))*unp.sqrt(L/C)/10
print( q_t )#"U_0", U_0 , "U_c", U_c)
q_e= U_m/U_0

U_min = U_m/q_t
print( q_e , U_min)
