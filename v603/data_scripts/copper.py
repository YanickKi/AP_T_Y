import numpy as np 
import matplotlib.pyplot as plt 

theta, N = np.genfromtxt('data_scripts/EmissionCu.dat', unpack = True)

plt.plot(theta, N, '.', markersize = 0.5, label = r'$\text{Messwerte}$')
plt.vlines(x = 20.2,ymin = 0, ymax = 1599, linewidth = 0.3, label = r'$K_\beta \text{ Linie}$' , color = 'tab:orange')
plt.vlines(x = 22.5,ymin = 0, ymax = 5050, linewidth = 0.3, label = r'$K_\alpha\text{ Linie}$', color = 'tab:green')

plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$\text{N}$')
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/copper.pdf')


def energie(theta):
    return 6.626e-34 * 299792458 / (2 * 201.4e-12 * np.sin(theta) * 1.602e-19) 

def radians(theta):
    return theta/180 * np.pi

Ebeta  = energie(radians(20.2)) 
Ealpha = energie(radians(22.5)) 

print(f'Die Energie der beta Linie beträgt:  {Ebeta}')
print(f'Die Energie der alpha Linie beträgt: {Ealpha}')