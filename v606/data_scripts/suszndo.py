import numpy as np
from uncertainties import ufloat

###############     Nd      ###############

Uo, Ro, Um, Rm = np.genfromtxt('nd.txt', unpack = True)

Uo *= 1e-3 #in Volt umrechnen
Um *= 1e-3 #in Volt umrechnen
Ro *= 5e-3 #in Ohm umrechnen
Rm *= 5e-3 #in Ohm umrechnen
R3 = 1000  #R = 1kOhm
Q  = 9.2e-3 / (15.7e-2 * 7.24e3)
F  = 86.6e-6 #Spulenquerschnitt in m^2
deltaR = Ro - Rm
deltaU = (Uo - Um)
dRerr = ufloat(np.mean(deltaR), np.std(deltaR, ddof=1) / np.sqrt(len(deltaR)))
dUerr = ufloat(np.mean(deltaU), np.std(deltaU, ddof=1) / np.sqrt(len(deltaU)))
x = 2 * dRerr * F / (R3 * Q)
xU = 4 * F * dUerr / Q
print(dRerr)
print(dUerr)
print(x)
print(xU)
print(Q)
np.savetxt('suznd.txt', np.column_stack([Uo*1e3, Ro*1e3, Um*1e3, Rm*1e3, deltaR, deltaU]), fmt=['%.1f', '%.0f', '%.1f', '%.0f', '%.3f', '%.3f'])