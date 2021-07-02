import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
phase, Uwo, Uwi = np.genfromtxt('data_scripts/phase.txt', unpack = True)

def radians(theta):
    return theta/180 * np.pi


def f(phi, a, b, c, d):
    return a*np.cos(b*phi+c) + d

phase = radians(phase)
Uwi *= 20 #SI 


params, covariance_matrix = curve_fit(f, phase, Uwi, p0=(30, 1, 113.92815598932053, 86.57729155463478))
uncertainties = np.sqrt(np.diag(covariance_matrix))
 
x_plot = np.linspace(phase[0], phase[-1], 1000)

plt.plot(phase, Uwi, '.', label = 'Messwerte')
plt.plot(x_plot, f(x_plot, *params), label = 'Regressionskurve')
np.savetxt(
    'Uwi.txt',
    Uwo, 
    fmt='%.2f',
) 
 
 
plt.xlabel(r'$\Phi \mathbin{/} \si{\radian}$')
plt.ylabel(r'$U_\text{out, noise} \mathbin{/} \si{\milli\volt}$')

print(f'die Parameter noisy  sind: {params}.')
print(f'die Fehle noisy sind: {uncertainties}.')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Uwi.pdf')