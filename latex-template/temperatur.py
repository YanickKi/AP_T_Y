import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

t, T1, p1, T2, p2, N=np.genfromtxt('Daten.txt', unpack=True)
T1 = T1 + 273.15
T2 = T2 + 273.15
t *= 60

params1, covariance_matrix1 = np.polyfit(t, T1, deg=2, cov=True)
params2, covariance_matrix2 = np.polyfit(t, T2, deg=2, cov=True)
errors1 = np.sqrt(np.diag(covariance_matrix1))
errors2 = np.sqrt(np.diag(covariance_matrix2))

x = np.linspace(t[0], t[-1], 100)
#for name1, value1, error1 in zip('abc', params1, errors1):
#    print(f'{name1} = {value1} ± {error1}')
#for name2, value2, error2 in zip('abc', params2, errors2):
#    print(f'{name2} = {value2} ± {error2}')

plt.plot(t, T1, '.', label='$T_1$')
plt.plot(t, T2, '.', label='$T_2$')
plt.plot(x, params1[0] * x**2 + params1[1] * x + params1[2], label = 'Ausgleichskurve für $T_1$')
plt.plot(x, params2[0] * x**2 + params2[1] * x + params2[2], label = 'Ausgleichskurve für $T_2$')
plt.xlabel(r'$t\:/\: \si{\second}$')
plt.ylabel(r'$t \:/\: \si{\kelvin}$')
plt.legend(loc='best')

#in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/temperatur.pdf')
