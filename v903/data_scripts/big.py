import numpy as np
import matplotlib.pyplot as plt 


fifteen, thirty, sixty = np.genfromtxt('data_scripts/big.txt', unpack = True)

#build/

def rad(degree):
    return np.pi/180 * degree

def doppler(angle):
    return np.pi/2 - np.arcsin(np.sin(rad(angle)) * 1800/2700) 

def flowvelocity(angle, shift):
    return shift * 343.2 / (2 * 2e6 * np.cos(angle))

doppler1 = doppler(15)
doppler2 = doppler(30)
doppler3 = doppler(60)
#98.000 8.412 159.000 13.650 250.000 21.466

flowvelocity15 = flowvelocity(doppler1, fifteen)  * 1e3   #mm/s
flowvelocity30 = flowvelocity(doppler2, thirty)   * 1e3   #mm/s
flowvelocity60 = flowvelocity(doppler3, sixty)    * 1e3   #mm/s
shiftcos15 = fifteen/np.cos(doppler1)
shiftcos30 = thirty/np.cos(doppler2)
shiftcos60 = sixty/np.cos(doppler3)

np.savetxt('data_scripts/big_velocity.txt', np.column_stack([fifteen, flowvelocity15, thirty, flowvelocity30, sixty ,flowvelocity60]), fmt = '%.3f')


plt.plot(flowvelocity15, shiftcos15, '.', label = r'$\theta = \ang{15;;}$' )
plt.plot(flowvelocity30, shiftcos30, '.', label = r'$\theta = \ang{30;;}$' )
plt.plot(flowvelocity60, shiftcos60, '.', label = r'$\theta = \ang{60;;}$' )

plt.xlabel(r'$v \mathbin{/} \si{\milli\meter\second\tothe{-1}}$')
plt.ylabel(r'$\symup{\Delta} \nu \cos^{-1}(\alpha) \mathbin{/} \si{\hertz}$')
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/big.pdf')