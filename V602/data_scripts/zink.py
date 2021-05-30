import numpy as np
import matplotlib.pyplot as plt

theta, imp = np.genfromtxt('data_scripts/Zink.dat', unpack = True)
 
IK = min(imp) + (max(imp) - min(imp)) / 2
def f(x1, x2, y1, y2, ymax):
    x = np.array([x1, x2])
    y = np.array([y1, y2])
    params = np.polyfit(x, y, deg=1)
    print(f'Die Steigung von Zink ist {params[0]}')
    print(f'Der y-Achsenabschnitt von Zink ist {params[1]}')
    print(f'Die Schnittstelle bei Zink ist bei {ymax *1/params[0] - params[1]/params[0]}')
    print(f'IK ist bei Zink {IK}')
    plt.plot(x, params[0] * x + params[1], 'k', linewidth = 0.5)
    return ymax*1/params[0] - params[1]/params[0]

#f(18.6, 18.7, 65.0, 84.0, IK)

x = f(18.6, 18.7, 65.0, 84.0, IK)

plt.plot(theta, imp,'.')
#plt.vlines(x = 18.75, ymin = -1000, ymax = 78.5, color = 'tab:orange', label = r'$\text{Mitte der Absorptionskante}$')
plt.plot(x, IK, 'x', color = 'tab:orange', label = r'$I_K$')

plt.plot([18.1, 18.3, 18.4], [54, 54, 54], 'g.', label = 'Minium')
plt.plot(19, 102,  'r.', label = 'Maximum')

#plt.ylim(51, 125)
plt.xlabel(r'$\theta \mathbin{/} \si{\degree}$')
plt.ylabel(r'$N$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/zink.pdf')