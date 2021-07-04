import numpy as np 
import matplotlib.pyplot as plt    
UG, IS = np.genfromtxt('data_scripts/frankherz2.txt', unpack = True)

plt.plot(UG, IS, '--')
plt.plot(UG, IS, 'x', color = 'tab:orange')
plt.xlabel(r'$U_\text{A} \mathbin{/} \si{\volt}$')
plt.ylabel(r'$I_\text{S} \mathbin{/} \si{\nano\ampere}$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/frankherz2.pdf')