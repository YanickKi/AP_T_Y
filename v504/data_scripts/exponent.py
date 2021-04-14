import numpy as np
import matplotlib.pyplot as plt    
from scipy.optimize import curve_fit

U, I = np.genfromtxt('data_scripts/suctionflow25.txt', unpack=True)

def f (V, c, d):
    return c * V**d

params, covariance_matrix = curve_fit(f, U, I)

uncertainties = np.sqrt(np.diag(covariance_matrix))

x = np.linspace(0, U[-1])

plt.plot(x, f(x, *params), label =  'Regressionskurve')
plt.plot(U, I, '.',        label =  'Messdaten')

plt.xlabel(r'$ U \mathbin{/} \si{\volt}$')
plt.ylabel(r'$ I_{\text{A}6} \mathbin{/} \si{\milli\ampere}$')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/exponent.pdf')