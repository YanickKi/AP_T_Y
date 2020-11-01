
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp


t = np.array([600, 900, 1200, 2100])
N = np.array([120, 120, 120, 122])
T1 = np.array([306.05, 310.75, 314.55, 323.45])
T2 = np.array([289.35, 286.15, 283.55, 276.05])
p1 = np.array([8.0, 9.0, 10.0, 12.0])
p2 = np.array([4.0, 3.6, 3.4, 3.2])
Terr = np.array([0.2, 0.2, 0.2, 0.2])




p1*= 100000
p2*= 100000


A1 = ufloat(-3.22e-6, 0.04e-6)
B1 = ufloat(20.28e-3, 0.09e-3)
C1 = ufloat(294.97, 0.04)
A2 = ufloat(0.95e-6, 0.07e-6)
B2 = ufloat(-11.21e-3, 0.1e-3)
dT1 = 2 * A1 * t + B1 
dT2 = 2 * A2 * t + B2
T1e = unp.uarray(T1, Terr)
T2e = unp.uarray(T2, Terr)
L   = ufloat(169e3,5e3)
K = 1.14

dm = (4 * 4186 + 720) * dT2 / L
dm *= 1e3
rho0 = 5510 # g / m^3
rho = p2 * rho0 * 273.15 / (100000 * T2e)
Nmech = (1 / (K - 1)) * (p1 * (p2 / p1)**(1./1.14) - p2) * dm / rho

nure = (4 * 4186 + 720) * dT1 / N
nuid = T1e / (T1e - T2e)
#atio = nure/nuid
#print(f'rho = {rho}')
print(f'Nmech = {Nmech}')
#print(f'dT2 = {dT2}')
