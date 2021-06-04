import numpy as np
from uncertainties import ufloat


###############     Dy      ###############

Uo, Ro, Um, Rm = np.genfromtxt('dy.txt', unpack = True)

Uo *= 1e-4
Um *= 1e-4
Ro *= 5e-3 #in Ohm umrechnen
Rm *= 5e-3 #in Ohm umrechnen

R3 = 1000   #R = 1kOhm
Q  = 14.38e-3 / (15.5e-2 * 7.8e3)
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
np.savetxt('suzdy.txt', np.column_stack([Uo*1e3, Ro*1e3, Um*1e3, Rm*1e3, deltaR, deltaU]), fmt=['%.1f', '%.0f', '%.1f', '%.0f', '%.3f', '%.3f'])