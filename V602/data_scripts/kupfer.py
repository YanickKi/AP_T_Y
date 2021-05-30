import numpy as np
import matplotlib.pyplot as plt

theta, Imp = np.genfromtxt('data_scripts/Emissionsspektrum.dat', unpack = True)

plt.plot(theta, Imp, '.', markersize = 0.8)

plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.vlines(theta[np.argmax(Imp)], ymin = -1000, ymax = np.max(Imp), linewidth=0.25, color = 'tab:green', label = r'$K_\alpha \text{ Linie}$')
plt.vlines(x = 20.2, ymin = -1000, ymax = 1599, linewidth=0.25, color = 'tab:orange', label = r'$K_\beta \text{ Linie}$')
plt.hlines(xmin = 22.35537, xmax = 22.84919, y = 0.5 * 5050, linewidth = 0.25, linestyles = 'dashed', color = 'tab:purple', label = r'$\symup{\Delta}K_\alpha$')
plt.hlines(xmin = 20.06083, xmax = 20.55552, y = 0.5 * 1599, linewidth = 0.25, linestyles = 'dashed', color = 'tab:red', label = r'$\symup{\Delta}K_\beta$')


def f(x1, x2, y1, y2, ymax, string):
    x = np.array([x1, x2])
    y = np.array([y1, y2])
    params = np.polyfit(x, y, deg=1)
    #print(f'Die Steigung von {string} ist {params[0]}')
    #print(f'Der y-Achsenabschnitt von {string } ist {params[1]}')
    print(f'Die Schnittstelle von {string} ist bei {ymax/2 *1/params[0] - params[1]/params[0]}')
    return ymax/2 *1/params[0] - params[1]/params[0]

xl1=f(20.0, 20.1, 291.0, 1127.0, 1599, 'links links')
xl2=f(20.6, 20.5, 425.0, 1267.0, 1599, 'links rechts')
print(f'Die Breite von links ist {xl2-xl1}')

xr1=f(22.3, 22.4, 536.0, 4128.0, 5050.0, 'rechts links')
xr2=f(22.9, 22.8, 901.0, 4097.0, 5050.0, 'rechts rechts')
print(f'Die Breite von rechts ist {xr2-xr1}')

plt.ylim(-100, 5250)

print(f'std error of the entries {np.std(theta)}')
#(Imp[np.where(theta == 20.5)] - Imp[np.where(theta == 19.9)])

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Kupfer.pdf')