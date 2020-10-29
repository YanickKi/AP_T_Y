import matplotlib.pyplot as plt
import numpy as np

t, T1, p1, T2, p2, N=np.genfromtxt('Daten.txt', unpack=True)

plt.plot(t, T1+273.15, label='$T_1$')
plt.plot(t, T2+273.15, label='$T_2$')
plt.xlabel(r'$t\:/\: \si{\minute}$')
plt.ylabel(r'$t \:/\: \si{\kelvin}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/temperatur.pdf')
