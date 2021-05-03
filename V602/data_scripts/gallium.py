import numpy as np
import matplotlib.pyplot as plt

theta, imp = np.genfromtxt('data_scripts/Gallium.dat', unpack = True)

plt.plot(theta, imp,'.')
plt.vlines(x = 17.35, ymin = -1000, ymax = 93.5, color = 'tab:orange', label = r'$\text{Mitte der Absorptionskante}$')

plt.ylim(63, 125)
plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/gallium.pdf')