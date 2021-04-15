import numpy as np
import matplotlib.pyplot as plt    
from scipy.optimize import curve_fit
from uncertainties import ufloat

#I in 20mA

U, I = np.genfromtxt('data_scripts/suctionflow25.txt', unpack=True)

#I in mA

I *= 20

def f (V, c, d):
    return c * V**d

index = [-1, -2]

new_U = np.delete(U, index)
new_I = np.delete(I, index)


params, covariance_matrix = curve_fit(f, new_U, new_I)


uncertainties = np.sqrt(np.diag(covariance_matrix))

x = np.linspace(new_U[0], new_U[-1])

plt.plot(x, f(x, *params), label =  'Regressionskurve')
plt.plot(U, I, '.',        label =  'Messdaten')

plt.xlabel(r'$ U \mathbin{/} \si{\volt}$')
plt.ylabel(r'$ I_{\text{A}6} \mathbin{/} \si{\milli\ampere}$')

print(f' c= {params[0]} pm {uncertainties[0]}')
print(f' d= {params[1]} pm {uncertainties[1]}')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/exponent.pdf')