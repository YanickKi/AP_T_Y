import numpy as np 
import matplotlib.pyplot as plt    
UG, IS = np.genfromtxt('wendepunkt2.txt', unpack = True)

plt.plot(UG, IS, '.', label = 'Raumtemperatur')
plt.xlabel('UG')
plt.ylabel('IS')

plt.legend()
plt.savefig('wendepunkt2.pdf')