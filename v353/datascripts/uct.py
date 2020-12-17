import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

t, U = np.genfromtxt('datascripts/uct.txt', unpack = True)
U       += 3.1
t       *= 0.2
tf      = np.delete(t, -1) 
lnu     = np.log(U)/3.1
lnuf    = np.delete(lnu, -1)

params1, covariance_matrix1 = np.polyfit(t, lnu, deg=1, cov=True)
errors1= np.sqrt(np.diag(covariance_matrix1))

params2, covariance_matrix2 = np.polyfit(tf, lnuf, deg=1, cov=True)
errors2= np.sqrt(np.diag(covariance_matrix2))

aerr = ufloat(params2[0], errors2[0])

x = np.linspace(t[0], t[-1])
y = np.linspace(tf[0], tf[-1])

plt.plot(x, x * params1[0] + params1[1], label = 'Gesamte Ausgleichsgerade')
plt.plot(y, y * params2[0] + params2[1], label = 'Kritische Ausgleichsgerade')
plt.plot(t, lnu, '.',  label = 'Messdaten')

plt.xlabel(r'$t \mathbin{/} \si{\milli\second}$')
plt.ylabel(r'$\ln \left (U / U_0 \right )$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/uct.pdf')

print(f'Steigung der gesamten Gerade {params1[0]} pm {np.sqrt(np.diag(covariance_matrix1))}')
print(f'Steigung der kritischen Gerade {params2[0]} pm {np.sqrt(np.diag(covariance_matrix2))}')
print(f'y-Achsenabschnitt der kritischen Gerade {params2[1]} pm {np.sqrt(np.diag(covariance_matrix2))}')
print(f'RC = { - 1 / aerr}')