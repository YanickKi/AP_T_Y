import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit

w, a, b = np.genfromtxt('datascripts/phasefreq.txt', unpack = True)

phi = a / b * 2 * np.pi
A = -np.sin(phi) / (w * 0.007165308633498797)
#phi /= 2 * np.pi
#phi *= 360
AU = A / 6.4

plt.polar(phi, AU)

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/polar.pdf')