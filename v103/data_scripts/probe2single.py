import numpy as np 
import matplotlib.pyplot as plt

x, D = np.genfromtxt('data_scripts/probe2single.txt', unpack = True)

x *= 1e-2
D *= 1e-3

linear = 0.601*x**2 - x**3/3


params, covariance_matrix = np.polyfit(linear, D, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

x_plot = np.linspace(linear[0], linear[-1], 1000)
D *= 1e3
plt.plot(linear, D, '.', label='Messwerte')
plt.plot(x_plot, (params[0] * x_plot + params[1]) * 1e3, label = 'Regressionsgerade')

plt.xlabel(r'$Lx^2-x^3 \mathbin{/} \si{\metre}$')
plt.ylabel(r'$D \mathbin{/} \si{\milli\metre}$')
plt.legend()

print(f'der Paremter m von der Probe2 ist = {params[0]} pm {errors[0]}')
print(f'der Paremter b von der Probe2 ist = {params[1]} pm {errors[1]}')


plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/probe2single.pdf')