import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
t, T1, p1, T2, p2, N=np.genfromtxt('Daten.txt', unpack=True)
T1 = T1 + 273.15
T2 = T2 + 273.15
T1 = 1 / T1
p1 = p1 + 1
p1 = np.log(p1)
params, covariance_matrix = np.polyfit(T1, p1, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

#for name, value, error in zip('abc', params, errors):
#    print(f'{name} = {value} ± {error}')

aerr = ufloat(params[0], errors[0])
Rerr = ufloat(-8.314462, 0.0)
Lerr = Rerr * aerr
print (Lerr / 120.91)
x = np.linspace(T1[0], T1[-1], 100)
plt.plot(T1, p1, '.', label = 'Daten')                                                                                        
plt.plot(x, params[0] * x + params[1], label = 'Ausgleichsgerade')                                    
plt.xlabel(r'$\frac{1}{T} \:/\: \si{\kelvin\tothe{-1}}$')
plt.ylabel(r'$\ln (p)')
plt.legend(loc='best')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Verdampfungswaerme.pdf')