import numpy as np 
import matplotlib.pyplot as plt    
UG, IS = np.genfromtxt('frankherz2.txt', unpack = True)
IS *= 0.01
plt.plot(UG, IS, '--', label = '175')
plt.xlabel('UA')
plt.ylabel('IS')

plt.legend()
plt.savefig('frankherz2.pdf')