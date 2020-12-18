import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit

w, a, b = np.genfromtxt('datascripts/phasefreq.txt', unpack = True)

phi = a / b * 2 * np.pi
A = -np.sin(phi) / (w * 0.007165308633498797) *  6.4
#phi /= 2 * np.pi
#phi *= 360
AU = A / 6.4

A2 = 1 / np.sqrt(1 + w**2 * (0.007165308633498797)**2)

AU2 = A2/6.4

x = np.linspace(w[0], w[-1], 10000)

plt.polar(phi, AU2, '.', label = 'Messdaten')
phi = np.arcsin(((x*0.007165308633498797)/(np.sqrt(1+x**2*(0.007165308633498797)**2))))
A = 1/(np.sqrt(1+x**2*(0.007165308633498797)**2))
A /= 6.4
plt.polar(phi, A, label = 'Berechnete Amplitude')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/polar.pdf')