import numpy as np
import matplotlib.pyplot as plt 


distance, shiftlow, intesitylow  = np.genfromtxt('data_scripts/profilelow.txt' , unpack = True)
distance, shifthigh, intesityhigh= np.genfromtxt('data_scripts/profilehigh.txt', unpack = True)


def rad(degree):
    return np.pi/180 * degree

def doppler(angle):
    return np.pi/2 - np.arcsin(np.sin(rad(angle)) * 1800/2700) 

def flowvelocity(angle, shift):
    return shift * 343.2 / (2 * 2e6 * np.cos(angle))

doppler1 = doppler(15)

flowvelocitylow  = flowvelocity(doppler1, shiftlow)       * 1e3   #mm/s
flowvelocityhigh = flowvelocity(doppler1, shifthigh)      * 1e3   #mm/s

np.savetxt('data_scripts/velocity.txt', np.column_stack([flowvelocitylow, flowvelocityhigh]), fmt = '%.3f')


plt.plot(distance, flowvelocitylow, '.', label = r' $5040 \, \text{rpm}$' )
plt.plot(distance, flowvelocityhigh, '.', label = r'$6110 \, \text{rpm}$' )

plt.xlabel(r'$d \mathbin{/} \si{\micro\second}$')
plt.ylabel(r'$v \mathbin{/} \si{\milli\meter\second\tothe{-1}}$')

plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/velocity.pdf')