import numpy as np 
import uncertainties.unumpy as unp 
import scipy.constants as const
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
import matplotlib.pyplot as plt


U, N, I = np.genfromtxt('data_scripts/Zaehlrohrstrom.dat', unpack = True)
Ierr = unp.uarray(I, 0.05) ## Strom in µ
Z = Ierr / (const.epsilon_0 * N)

#print(Z)

Zoerr = np.array([3444370.4402958797, 4519896.217600876, 7702517.022224408, 8900869.410879867, 11090034.047260595, 14320021.33604725, 15068833.453942882,  17605753.193655793])
Zerr  = np.array([574061.7400493133, 564987.0272001096, 550179.7873017435, 556304.3381799916, 554501.7023630298, 550770.0513864327, 538172.623355103, 489048.699823772])

plt.errorbar(I, Zoerr, yerr = Zerr, fmt = '.')

plt.xlabel(r'$I \mathbin{/} \si{\micro\ampere}$')
plt.xlabel(r'$I \mathbin{/} \si{\micro\ampere}$')
plt.ylabel(r'$Z$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/cur.pdf')