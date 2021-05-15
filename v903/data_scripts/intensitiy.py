import numpy as np
import matplotlib.pyplot as plt 


distance, shiftlow,  intesitylow  = np.genfromtxt('data_scripts/profilelow.txt' , unpack = True)
distance, shifthigh, intesityhigh = np.genfromtxt('data_scripts/profilehigh.txt', unpack = True)

plt.plot(distance, intesitylow, '.', label = r' $5040 \, \text{rpm}$' )
plt.plot(distance, intesityhigh, '.', label = r'$6110 \, \text{rpm}$' )

plt.xlabel(r'$d \mathbin{/} \si{\micro\second}$')
plt.ylabel(r'$I$')

plt.legend(loc = 'upper left')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/intensity.pdf')