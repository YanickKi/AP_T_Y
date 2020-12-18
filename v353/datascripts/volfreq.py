import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit

w, U = np.genfromtxt('datascripts/volfreq.txt', unpack = True)
U /= 6.4

def f(x, T):
    return 1 / np.sqrt(1 + x**2 * T**2)

params, covariance_matrix =  curve_fit(f, w, U)

z = np.linspace(w[0], w[-1], 10000)
 
plt.plot(w, U,'.', label = 'Messdaten')
plt.plot(z, f(z, *params), label = 'Fit')

plt.xscale('log')
plt.xlabel(r'$\omega \mathbin{/} \si{\hertz}$')
plt.ylabel(r'$\sfrac{U_\text{C}} {U_0} $')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/ucw.pdf')

print(f' T = {params[0]} pm {np.sqrt(np.diag(covariance_matrix))}')