import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
x, U = np.genfromtxt('data_scripts/distance.txt', unpack = True)

def firstorder(r, a, b):
    return a / r + b

def secondorder(r, a, b):
    return a / r**2 + b

r = 138 - x
U /= 2 # U in Volt

params_firstorder, covariance_matrix_firstorder = curve_fit(firstorder, r, U)
uncertainties_firstorder = np.sqrt(np.diag(covariance_matrix_firstorder))

params_secondorder, covariance_matrix_secondorder = curve_fit(secondorder, r, U)
uncertainties_secondorder = np.sqrt(np.diag(covariance_matrix_secondorder))

x_plot = np.linspace(r[0], r[-1], 1000)

plt.plot(r, U, '.', label = 'Messwerte')
plt.plot(x_plot, firstorder(x_plot, *params_firstorder), label = r'$\propto \frac{1}{r}$')
plt.plot(x_plot, secondorder(x_plot, *params_secondorder), label = r'$\propto \frac{1}{r²}$')
np.savetxt(
    'distance_parameter.txt',
    np.column_stack([params_firstorder, uncertainties_firstorder, params_secondorder, uncertainties_secondorder]), 
    fmt='%.2f',
) 

np.savetxt(
    'distance_voltage.txt',
    np.column_stack([r, U]), 
    fmt='%.2f',
) 

plt.xlabel(r'$r \mathbin{/} \si{\centi\metre}$')
plt.ylabel(r'$U \mathbin{/} \si{\volt}$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/distance.pdf')