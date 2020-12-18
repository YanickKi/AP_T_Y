import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit

w, a, b = np.genfromtxt('datascripts/phasefreq.txt', unpack = True)

phi = a / b * 2 * np.pi

def f(x, T):
    return np.arctan(-x * T)

params, covariance_matrix =  curve_fit(f, w, phi)

z = np.linspace(w[0], w[-1], 10000)
 
plt.plot(w, phi,'.', label = 'Messdaten')
plt.plot(z, f(z, *params), label = 'Fit')

plt.xscale('log')
plt.xlabel(r'$\omega \mathbin{/} \si{\hertz}$')
plt.ylabel(r'$\varphi \mathbin{/} \si{\radian} $')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/phasefreq.pdf')
print(f'RC = {params[0]} pm {np.sqrt(np.diag(covariance_matrix))}')
#print(f' T = {params[0]} pm {np.sqrt(np.diag(covariance_matrix))}')