import numpy as np
import matplotlib.pyplot as plt

t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data_scripts/dynamisch40.txt', unpack = True)
T1 += 273.15
T2 += 273.15
T3 += 273.15
T4 += 273.15
T5 += 273.15
T6 += 273.15
T7 += 273.15
T8 += 273.15

plt.plot(t*2, T1, label = r'$T_1$')
plt.plot(t*2, T2, label = r'$T_2$')

plt.xlabel(r'$t \mathbin{/} \si{\second}$')
plt.ylabel(r'$T \mathbin{/} \si{\kelvin}$')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Me.pdf')