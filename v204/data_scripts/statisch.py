import numpy as np
import matplotlib.pyplot as plt

t, T1, T4, T5, T8, T2, T3, T6, T7 = np.genfromtxt('data_scripts/statisch.txt', unpack = True)

plt.plot(t / 10, T1, label = 'T1')
plt.plot(t / 10, T4, label = 'T4')
plt.plot(t / 10, T7, label = 'T7')
plt.plot(t / 10, T8, label = 'T8')

plt.xlabel('t / s')
plt.ylabel('T / C')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/statisch.pdf')