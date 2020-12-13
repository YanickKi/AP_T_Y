import numpy as np
import matplotlib.pyplot as plt

t, U = np.genfromtxt('Uct.txt', unpack = True)
U += 3.1
lnu = np.log(U)

plt.plot(t, lnu)
#plt.yscale('log')
plt.savefig('uct.pdf')
print(lnu)

