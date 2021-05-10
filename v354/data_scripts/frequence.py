import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp

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

L = ufloat(16.78e-3, 0.09e-3)
C = ufloat(2.066e-9, 0.06e-9)
R = ufloat(67.2, 0.2)

wplus =     R / (4 * np.pi * L) + 1 / (2 * np.pi) * unp.sqrt(1 / ( L * C) + R**2 / (4 * L**2))
wminus = -  R / (4 * np.pi * L) + 1 / (2 * np.pi) * unp.sqrt(1 / ( L * C) + R**2 / (4 * L**2))
print(f'Der theoretische Wert für omega+ ist {wplus:.2f} ')
print(f'Der theoretische Wert für omega- ist {wminus:.2f} ')
print(f'Die theoretische Güte beträgt {unp.sqrt(L/C) / R:.2f}')
print(f'Die theoretische Breit ist : {wplus - wminus}')

##