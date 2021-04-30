import numpy as np
import matplotlib.pyplot as plt    
from scipy.optimize import curve_fit
from uncertainties import ufloat

#I in nA
#data_scripts/
U, I = np.genfromtxt('data_scripts/reversevoltage.txt', unpack=True)

index = [-1,-2]
new_I = np.delete(I, index)
new_U = np.delete(U, index)

new_I /= 10**(9)

new_U = new_U + 1000000 * new_I
##
plt.plot(new_U, np.log(new_I), '.', label =  'Messdaten')

#new_I = np.delete(new_I, [0,1])
#new_U = np.delete(new_U, [0,1])

params, covariance_matrix = np.polyfit(new_U, np.log(new_I), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

x = np.linspace(new_U[2],new_U[-1])

plt.plot(x, params[0]*x + params[1], label =  'Regressionsgerade')


plt.xlabel(r'$ U \mathbin{/} \si{\volt}$')
plt.ylabel(r'$ \ln \left ( I_{\text{A}6} \right )')

m_err = ufloat(params[0], errors[0])

T_err = -1.602*10**(-19) / (1.380649*10**(-23) *  m_err)

print(T_err)

print(f' params[0]= {params[0]} pm {errors[0]}')
print(f' params[1]= {params[1]} pm {errors[1]}')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/startcurr.pdf')