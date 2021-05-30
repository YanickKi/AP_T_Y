import numpy as np
import matplotlib.pyplot as plt

theta, Imp = np.genfromtxt('data_scripts/Emissionsspektrum.dat', unpack = True)

plt.plot(theta, Imp, '.', markersize = 0.8)

plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.vlines(theta[np.argmax(Imp)], ymin = -1000, ymax = np.max(Imp), linewidth=0.25, color = 'tab:green', label = r'$K_\alpha \text{ Linie}$')
plt.vlines(x = 20.2, ymin = -1000, ymax = 1599, linewidth=0.25, color = 'tab:orange', label = r'$K_\beta \text{ Linie}$')
plt.hlines(xmin = 22.2, xmax = 22.8, y = 0.5 * 5050, linewidth = 0.25, linestyles = 'dashed', color = 'tab:purple', label = r'$\symup{\Delta}K_\alpha$')
plt.hlines(xmin = 19.9, xmax = 20.5, y = 0.5 * 1599, linewidth = 0.25, linestyles = 'dashed', color = 'tab:red', label = r'$\symup{\Delta}K_\beta$')


def f(x1, x2, y1, y2, string):
    x = np.array([x1, x2])
    y = np.array([y1, y2])
    params = np.polyfit(x, y, deg=1)
    print(f'Die Steigung von {string} ist {params[0]}')
    print(f'Der y-Achsenabschnitt von {string } ist {params[1]}')
    
f(20.0, 20.1, 291.0, 1127.0, 'links links')

plt.ylim(-100, 5250)

print(f'std error of the entries {np.std(theta)}')
#(Imp[np.where(theta == 20.5)] - Imp[np.where(theta == 19.9)])

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Kupfer.pdf')