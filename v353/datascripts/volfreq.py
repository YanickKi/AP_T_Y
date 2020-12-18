import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit

w, U = np.genfromtxt('datascripts/volfreq.txt', unpack = True)
U *= 2 
U /= 6.4    

def f(x, T, b):
    return 6.4 / np.sqrt(1 + x**2 * T**2)

params, covariance_matrix =  curve_fit(f, w, U)

z = np.linspace(w[0], w[-1], 1000)
 
plt.plot(w, U,'.', label = 'Messdaten')
plt.plot(z, f(z, *params))

plt.xscale('log')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/ucw.pdf')