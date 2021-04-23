import numpy as np

I = np.genfromtxt('pressure.txt', unpack = True)

n = 1 + I * 635 * 1e-9 / (2 * 50 * 1e-3) * 293.15 / 273.15 * 1.0132 / 0.7999

np.savetxt('fractionindex.txt', np.column_stack([n]), fmt='%2.8f')
print(f'mean of the index: {np.mean(n)}')
print(f'error of  the entries:{np.std(n)}')
print(f'error of the mean:{np.std(n, ddof=1) / np.sqrt(len(n))}')