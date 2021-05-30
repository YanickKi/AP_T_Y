import numpy as np
import matplotlib.pyplot as plt

theta, imp = np.genfromtxt('data_scripts/Brom.dat', unpack = True)

IK = min(imp) + (max(imp) - min(imp)) / 2
def f(x1, x2, y1, y2, ymax):
    x = np.array([x1, x2])
    y = np.array([y1, y2])
    params = np.polyfit(x, y, deg=1)
    print(f'Die Steigung von Brom ist {params[0]}')
    print(f'Der y-Achsenabschnitt von Brom ist {params[1]}')
    print(f'Die Schnittstelle bei Brom ist bei {ymax *1/params[0] - params[1]/params[0]}')
    print(f'IK ist bei Brom {ymax}')
    plt.plot(x, params[0] * x + params[1], 'k', linewidth = 0.5)
    return ymax*1/params[0] - params[1]/params[0]
 
x = f(13.1, 13.2, 13, 18, IK)

plt.plot(theta, imp,'.')
plt.plot(x, IK, 'x', color = 'tab:orange', label = r'$I_K$')

plt.plot(13, 9, 'g.', label = 'Minium')
plt.plot([13.5, 13.6], [27, 27],  'r.', label = 'Maximum')

plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/brom.pdf')