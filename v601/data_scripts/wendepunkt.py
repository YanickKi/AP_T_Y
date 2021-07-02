import numpy as np 
import matplotlib.pyplot as plt    
UG, IS = np.genfromtxt('wendepunkt.txt', unpack = True)

IS *= 0.01
plt.plot(UG, IS, '.', label = 'Raumtemperatur')
plt.xlabel('UG')
plt.ylabel('IS')

plt.legend()
plt.savefig('wendepunkt.pdf')