import numpy as np
import matplotlib.pyplot as plt

t, T1, T4, T5, T8, T2, T3, T6, T7 = np.genfromtxt('data_scripts/dynamisch40.txt', unpack = True)


plt.plot(t*2, T1, label = 'T1')
plt.plot(t*2, T2, label = 'T2')

plt.xlabel('t / s')
plt.ylabel('T / C')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/dynamisch40.pdf')