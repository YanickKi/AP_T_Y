import numpy as np
import matplotlib.pyplot as plt

theta, imp = np.genfromtxt('data_scripts/Strontium.dat', unpack = True)
 
IK = min(imp) + (max(imp) - min(imp)) / 2
def f(x1, x2, y1, y2, ymax):
    x = np.array([x1, x2])
    y = np.array([y1, y2])
    params = np.polyfit(x, y, deg=1)
    print(f'Die Steigung von Strontium ist {params[0]}')
    print(f'Der y-Achsenabschnitt von Strontium ist {params[1]}')
    print(f'Die Schnittstelle bei Strontium ist bei {ymax *1/params[0] - params[1]/params[0]}')
    print(f'IK ist bei Strontium {ymax}')
    plt.plot(x, params[0] * x + params[1], 'k', linewidth = 0.5)
    return ymax*1/params[0] - params[1]/params[0]

x = f(11, 11.1, 89, 120, IK)

plt.plot(theta, imp,'.')
plt.plot(x, IK, 'x', color = 'tab:orange', label = r'$I_K$')

plt.plot(10.7, 40, 'g.', label = 'Minium')
plt.plot(11.6, 196,  'r.', label = 'Maximum')

plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/strontium.pdf')