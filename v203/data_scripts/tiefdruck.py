import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat

p, Tl, Tw = np.genfromtxt('data_scripts/tiefdruck.txt', unpack = True)

p *= 1e-2 #p in SI
p0 = 1e5 #atomespheric pressure
Tl += 273.15 #Tl in SI
R = 8.31446261815324 #general gas constant

params, covariance_matrix = np.polyfit(1/Tl, np.log(p/p0), deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))
 
m = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

x_plot = np.linspace(1/Tl[0], 1/Tl[-1], 1000)

plt.plot(1/Tl, np.log(p/p0), '.', label ='Messwerte')
plt.plot(x_plot, params[0] * x_plot + params[1], label ='Regressionsgerade')

plt.xlabel(r'${T_\text{g}}^{-1} \mathbin{/} \si{\kelvin\tothe{-1}}$')
plt.ylabel(r'$\ln \left ( \sfrac{p}{p_0} \right )$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/tiefdruck.pdf')

L = - m * R #heat of evaporation 


print(f'Die Steigung der Ausgleichsgeraden Tiefdruck ist {m:.2f}')
print(f'Der Achsenabschnitt der Ausgleichsgeraden Tiefdruck ist {b:.2f}')
print(f'Die Verdampfungswärme beträgt {L}')