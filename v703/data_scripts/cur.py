import numpy as np 
import uncertainties.unumpy as unp 
import scipy.constants as const
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import matplotlib.pyplot as plt


U, N, I = np.genfromtxt('data_scripts/Zaehlrohrstrom.dat', unpack = True) # I in µA
I *= 10**(-6) # I in A 
N /= 60

Nerr = unp.uarray(N, np.sqrt(N))

Ierr = unp.uarray(I, 0.05 * 10**(-6))
Z = Ierr / (const.elementary_charge * Nerr)

I *= 10**6 # I in µA

Zoerr = np.array([11420876622.984013, 14987115336.374016, 25540080000.716293, 29513588372.979668, 36772441522.746056, 47482464430.69732, 49965382850.9200,  58377325715.92296])
Zerr  = np.array([1903479437.1640024, 1873389417.046752, 1824291428.6225922, 1844599273.3112292, 1838622076.13730264, 1826248631.9498968, 1784477958.9614303, 1621592380.99786])

print(Z * 10**(-9))

Zoerr *= 10**(-9)
Zerr  *= 10**(-9)
plt.errorbar(I, Zoerr, yerr = Zerr, fmt = '.')

plt.xlabel(r'$I \mathbin{/} \si{\micro\ampere}$')
plt.ylabel(r'$Z$ in Mrd.')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/cur.pdf')