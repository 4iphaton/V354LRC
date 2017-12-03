import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import scipy.constants as const
import math

a= ufloat(-2.64611770 , 0.148322358 )*(10**(4))
L = ufloat(10.11 , 0.03)*(10 **(-3))
T_ex= -1/a
R_eff = - 2*L*a

print ("a", a, "T_ex", T_ex, "R_eff", R_eff)
