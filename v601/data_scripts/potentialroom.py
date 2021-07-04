import numpy as np 
import matplotlib.pyplot as plt    
UG, IS = np.genfromtxt('data_scripts/wendepunkt2.txt', unpack = True)

k = 0

y = np.zeros(len(UG) -1 )
x = np.zeros(len(UG) -1 )

while(k < len(UG) - 1):
    y[k] = abs((IS[k+1] - IS[k])/ (UG[k+1] - UG[k]))
    #y[k] = (IS[k] - IS[k+1])
    x[k] = UG[k] + (UG[k+1] - UG[k])/2
    k += 1


plt.plot(x, y, '.')
plt.plot(x[8], max(y),'.', label = 'Maximum')
plt.ylabel(r'$ \left | \frac{\symup{\Delta}I_\text{A}}{\symup{\Delta}U_\text{A}} \right | \mathbin{/} \si{\nano\ampere\volt\tothe{-1}}$')
plt.xlabel(r'$U_\text{A} \mathbin{/} \si{\volt}$')

print(x[8])
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/potentialroom.pdf')