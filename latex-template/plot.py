import matplotlib.pyplot as plt
import numpy as np

x,y1,p1,y2,p2,w=np.genfromtxt('Daten.txt', unpack=True)

plt.subplot(1, 2, 1)
plt.plot(x, y1+273.15, label='$T_1$')
plt.plot(x, y2+273.15, label='$T_2$')
plt.xlabel(r'$t\:/\: \si{\minute}$')
plt.ylabel(r'$t \:/\: \si{\kelvin}$')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.plot(x,p1,label='$P_1$')
plt.plot(x,p2,label='$P_2$')
plt.xlabel(r'$t \:/\: \si{\minute}$')
plt.ylabel(r'$p \:/\: \si{\bar}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
