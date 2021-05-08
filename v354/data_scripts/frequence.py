import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

f, UErr,  Uc = np.genfromtxt('data_scripts/frequence.txt', unpack = True)
UErr *= 5
Uc *= 10

U = Uc / UErr

plt.hlines(xmin = f[0], xmax = f[-1], y = max(U) / np.sqrt(2), linestyle = '--', color = 'tab:red', label = r'$\sfrac{U_\text{max}}{\sqrt{2}}$' )
plt.plot(f, U, '.', markersize = 2, label = 'Messwerte')
plt.xscale('log')
plt.yscale('log')

plt.xlabel(r'$\nu   \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$U     \mathbin{/} \si{\volt}$')
plt.legend(loc = 'center left')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/frequence.pdf')
np.savetxt('quotientUcUErr.txt', np.column_stack([f, UErr, Uc, U]), fmt = '%2.2f', header='v, UErr, Uc, U')