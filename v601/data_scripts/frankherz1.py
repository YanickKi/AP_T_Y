import numpy as np 
import matplotlib.pyplot as plt    
UG, IS = np.genfromtxt('frankherz1.txt', unpack = True)

plt.plot(UG, IS, '.', label = '165')
plt.xlabel('UA')
plt.ylabel('IS')

plt.legend()
plt.savefig('frankherz1.pdf')