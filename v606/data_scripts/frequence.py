import numpy as np 
import matplotlib.pyplot as plt 

w, UE = np.genfromtxt('data_scripts/frequence.txt', unpack = True)

UE /= 10 #Verstärkung rausnehmen

U =  UE/0.01

plt.plot(w, U, '.', label = 'Messwerte')


plt.xlabel(r'$\nu \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$U_\text{A}U_\text{E}^{-1}$')
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/frequence.pdf')