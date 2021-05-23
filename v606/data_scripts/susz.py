import numpy as np


###############     Dy      ###############

Uo, Ro, Um, Rm = np.genfromtxt('dy.txt', unpack = True)

Uo *= 1e-3
Um *= 1e-3
Ro *= 5e-3 #in Ohm umrechnen
Rm *= 5e-3 #in Ohm umrechnen

R3 = 1000   #R = 1kOhm
Q  = 0.8 * 5.5  * 1e-4 #Probenquerschnitt in m^2
F  = 86.6 * 1e-6 #Spulenquerschnitt in m^2
deltaR = Ro - Rm

x = 2 * deltaR * F / (R3 * Q)

np.savetxt('suzdy.txt', np.column_stack([Uo*1e3, Ro*1e3, Um*1e3, Rm*1e3, deltaR, x*1e3]), fmt=['%.1f', '%.0f', '%.1f', '%.0f', '%.3f', '%.3f'])