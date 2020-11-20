import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from scipy.signal import find_peaks

t, T1, T4, T5, T8, T2, T3, T6, T7 = np.genfromtxt('data_scripts/statisch.txt', unpack = True)
T1 += 273.15
T2 += 273.15
T3 += 273.15
T4 += 273.15
T5 += 273.15
T6 += 273.15
T7 += 273.15
T8 += 273.15
T1e = unp.uarray(T1, 0.1)
T2e = unp.uarray(T2, 0.1)
T3e = unp.uarray(T3, 0.1)
T4e = unp.uarray(T4, 0.1)
T5e = unp.uarray(T5, 0.1)
T6e = unp.uarray(T6, 0.1)
T7e = unp.uarray(T7, 0.1)
T8e = unp.uarray(T8, 0.1)
Ag = 0.012 * 0.04
Ak = 0.007 * 0.04


TM = T1 - T2
TMK= T4 - T3
TA = T5 - T6
TE = T8 - T7

DM = unp.uarray([TM[1000], TM[2000], TM[3000], TM[5000], TM[7000]], 0.2) 
DMK= unp.uarray([TMK[1000], TMK[2000], TMK[3000], TMK[5000], TMK[7000]], 0.2) 
DA = unp.uarray([TA[1000], TA[2000], TA[3000], TA[5000], TA[7000]], 0.2)
DE = unp.uarray([TE[1000], TE[2000], TE[3000], TE[5000], TE[7000]], 0.2)
ka = np.array([120, 237, 21]) 


def DQDT(k, A , DT):
     return -k * A * DT / 0.03 

#print( A1[1] * A1[2])
#print( A2[1] * A2[2])

#print(DQDT(ka[0], Ag, DM))
#print(DQDT(ka[0], Ak, DMK))
#print(DQDT(ka[1], Ag, DA))
#print(DQDT(ka[2], Ag, DE))

peaks1, _ = find_peaks(T1, distance = 15)





qwodqw = np.array([9.44, 11.21, 11.50, 11.70, 12.12, 12.08, 12.22, 12.22, 12.37, 12.41])

#print(0.5 * qwodqw)