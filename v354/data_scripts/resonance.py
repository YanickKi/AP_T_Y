import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

f, UErr,  Uc = np.genfromtxt('data_scripts/frequence.txt', unpack = True)
UErr *= 5
Uc *= 10

U = Uc / UErr 
#
print(f'theoretische Güte =  {np.sqrt(16.78e-3/2.066e-9) / 67.2}')
print(f'Güte q = {26/(26.5-25.5)}')
f = f[np.where(U > max(U)/5)]
U = U[np.where(U > max(U)/5)]

print(f'test = {30.91/np.sqrt(2)}')

plt.plot(f, U, '.', label = r'$U > \sfrac{U_\text{max}}{\sqrt{2}}$')


plt.xlabel(r'$\nu   \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$U     \mathbin{/} \si{\volt}$')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/resonance.pdf')
#np.savetxt('quotientUcUErr.txt', np.column_stack([f, UErr, Uc, U]), fmt = '%2.2f', header='v, UErr, Uc, U')