import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

#t in 25µs, U in 5V
t, U = np.genfromtxt('data_scripts/voltage.txt', unpack = True)

t *= 25 * 1e-6 #t in s
U *= 5  #U in V


def f(t, U0, mu):
    return U0 * np.exp(- 2 * np.pi * mu * t)


params, covariance_matrix = curve_fit(f, t, U) # t in s
uncertainties = np.sqrt(np.diag(covariance_matrix))


x = np.linspace(t[0], t[-1], 1000) # t  und x in µs

t *= 1e6    #t in µs
#
plt.plot(x * 1e6, f(x, *params), label = 'Rekursionskurve')
plt.plot(t, U, '.', label = 'Messwerte')

plt.xlabel(r'$t \mathbin{/} \si{\micro\second}$')
plt.ylabel(r'$U \mathbin{/} \si{\volt}$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/voltage.pdf')


L = ufloat(16.78e-3, 9e-5 ) 
muerr = ufloat(params[1], uncertainties[1])

R = 4 * np.pi * muerr *  L

print(f' Der Regressionsparamter U0 ist{params[0]} pm {uncertainties[0]}')
print(f' Der Regressionsparamter µ  ist{params[1]} pm {uncertainties[1]}')
print(f' Der Dämpfunsgwiderstand R ist {R:.2f}')
print(f' Die Abklingdauer Tex ist {2 * L / R * 1e6:.2f}') #Abklingdauer in µs
np.savetxt('voltagetex.txt', np.column_stack([t, U]), fmt=['%3.3f', '%3.3f'],  delimiter=',   ', header='t,U')
