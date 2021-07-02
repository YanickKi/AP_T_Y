import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat

p, T= np.genfromtxt('data_scripts/hochdruck.txt', unpack = True)

p *= 1e5 #p in SI
T += 273.15
R = 8.31446261815324 #general gas constant

params, covariance_matrix = np.polyfit(T, p, deg=3, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
 
a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
c = ufloat(params[2], errors[2])
d = ufloat(params[3], errors[3])



x_plot = np.linspace(T[0], T[-1], 1000)

plt.plot(T, p, '.', label ='Messwerte')
plt.plot(x_plot, params[0] * x_plot**3 + params[1] * x_plot**2 + params[2] * x_plot + params[3], label ='Regressionsgerade')

plt.xlabel(r'$T \mathbin{/} \si{\kelvin}$')
plt.ylabel(r'$p \mathbin{/} \si{\pascal}$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/hochdruck.pdf', bbox_inches='tight')


print(f'Der Parameter a beim Hochdruck ist {a:.2f}')
print(f'Der Parameter b beim Hochdruck ist {b:.2f}')
print(f'Der Parameter c beim Hochdruck ist {c:.2f}')
print(f'Der Parameter d beim Hochdruck ist {d:.2f}')