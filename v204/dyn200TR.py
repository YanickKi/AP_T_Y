import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat 
t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data_scripts/dynamisch200.txt', unpack = True)
T1 += 273.15
T2 += 273.15
T3 += 273.15
T4 += 273.15
T5 += 273.15
T6 += 273.15
T7 += 273.15
T8 += 273.15

peaks7, _ = find_peaks(T7, distance = 30)
peaksm7, _ = find_peaks(-T7, distance = 30)
peaks8, _ = find_peaks(T8, distance = 30)
peaksm8, _ = find_peaks(-T8, distance = 30)

peaksm7s = np.array([103, 203, 303, 304])
peaks7s  = np.array([54, 154, 259, 354])
peaks8s  = np.array([94, 190, 287, 384])
peaksm8s = np.array([109, 213, 316, 418])

peaks7se  = unp.uarray([2*54, 2*154, 2*259, 2*354], 0.1)
peaksm7se = unp.uarray([103, 203, 303, 304], 0.1)
peaks8se  = unp.uarray([2*94, 2*190, 2*287, 2*384], 0.1)
peaksm8se = unp.uarray([109, 213, 316, 418], 0.1)
print(peaks8se - peaks7se)
T7y = unp.uarray(T7[peaks7s], 0.2) 
T7my = unp.uarray(T7[peaksm7s], 0.2) 
T8y = unp.uarray(T8[peaks8s], 0.2) 
T8my = unp.uarray(T8[peaksm8s], 0.2) 

A7 = T7y - T7my  
A8 = T8y - T8my

kappaA7 = 8000 * 400 * 0.03**2 / (2 * np.mean(peaks7se - peaks8se) * np.mean(unp.log(A7 / A8)))
print(np.mean(peaks8se - peaks7se))
#print(peaks7,  peaksm7)
print(A7)
#print(peaks8,  peaksm8)
print(0.5 * A8)
#print(unp.log(A7 / A8))
#print(kappaA7)
