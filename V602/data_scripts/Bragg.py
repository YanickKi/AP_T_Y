import numpy as np
import matplotlib.pyplot as plt

theta, Imp = np.genfromtxt('data_scripts/Bragg.dat', unpack = True)

print(f'Standardabweichung der Bragg-Winkel: {np.std(theta)}')

plt.plot(theta, Imp, '.')

plt.xlabel(r'$\theta_\text{GM} \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Bragg.pdf')