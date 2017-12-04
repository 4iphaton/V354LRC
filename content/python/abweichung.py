import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
import scipy.constants as const
from uncertainties import ufloat
import math

a_a1= ((48.1 - 535 )/48.1)*100
a_a2= ((509.5 - 535 )/509.5)*100
b_1= ((4390 - 3400 )/4390)*100

print(a_a1, "     ", a_a2, "     ", b_1)
