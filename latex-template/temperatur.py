import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

t, T1, p1, T2, p2, N=np.genfromtxt('Daten.txt', unpack=True)
T1 = T1 + 273.15
T2 = T2 + 273.15
def f(x, A, B, C):
    return A * x**2 + B * x + C

params1, pcov1 = curve_fit(f, t, T1)
params2, pcov2 = curve_fit(f, t, T2)

x = np.linspace(t[0], t[-1], 100)
#print(f'params1 = {params1}')
#print(f'params2 = {params2}')
                 #fit for T1
               #fit for T2
plt.plot(t, T1, '.', label='$T_1$')                             #Data T1                                   
plt.plot(t, T2, '.', label='$T_2$')                             #Data T2 
plt.plot(x, f(x, *params1), label = 'Ausgleichsgerade T1')      #fit for T1                      
plt.plot(x, f(x, *params2), label = 'Ausgleichsgerade T2')      #fit for T2                                     
plt.xlabel(r'$t\:/\: \si{\minute}$')
plt.ylabel(r'$t \:/\: \si{\kelvin}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/temperatur.pdf')
