import numpy as np
import matplotlib.pyplot as plt

U, N = np.genfromtxt('data_scripts/Kennlinie.dat', unpack = True)
Uplat, Nplat = np.genfromtxt('data_scripts/Kennlinieplat.dat', unpack = True)
N_error = np.sqrt(N)

params, covariance_matrix = np.polyfit(Uplat, Nplat, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))
x = np.linspace(Uplat[0], Uplat[-1])

plt.errorbar(U, N, yerr = N_error, fmt = '.', label = 'Teilchenzahl')
plt.plot(x, params[0] * x + params[1], label = 'Plateau-Ausgleichsgerade')

plt.xlabel(r'$U \mathbin{/} \si{\volt}$')
plt.ylabel(r'$N \mathbin{/} \si{\per\minute}$')
plt.legend()

# print(f'a = {params[0]} pm {errors[0]}')
# print(f'b = {params[1]} pm {errors[1]} 1')

#print(f'Zwei Werte:{params[0] * 400+ params[1]}, {params[0] * 400 + params[1]} ')
print(f'und dessen Verhältnis: {((params[0] * 600 + params[1]) - (params[0] * 500 + params[1])) / (600 - 500)}')
#print(f' {(3.0 * 300 + 88.67) / (3.0 * 400 + 88.67)}')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/char.pdf')