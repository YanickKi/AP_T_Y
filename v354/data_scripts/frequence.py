import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

f, UErr,  U = np.genfromtxt('data_scripts/frequence.txt', unpack = True)

plt.plot(f, U, '.')
plt.xscale('log')
plt.yscale('log')

plt.xlabel(r'$\nu   \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$U     \mathbin{/} \si{\volt}$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/frequence.pdf')
#np.savetxt('frequence.txt', np.column_stack([t, U]), fmt=['%3.3f', '%3.3f'],  delimiter=',   ', header='t,U')