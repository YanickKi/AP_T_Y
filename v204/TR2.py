import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat 
t, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data_scripts/dynamisch40.txt', unpack = True)
T1 += 273.15
T2 += 273.15
T3 += 273.15
T4 += 273.15
T5 += 273.15
T6 += 273.15
T7 += 273.15
T8 += 273.15

peaks1, _ = find_peaks(T5, distance = 15)
peaks2, _ = find_peaks(T6, distance = 15)


p1 = np.array([47.99, 54.9 , 58.58, 61.52, 64.14, 66.03, 67.95, 69.56, 71.01, 72.19])
p2 = np.array([38.55, 43.69, 47.08, 49.82, 52.02, 53.95, 55.73, 57.34, 58.64, 59.78])
t1 = np.array([48, 128, 208, 288, 368, 448, 528, 608, 688, 768])
t2 = np.array([74, 148, 224, 304, 382, 462, 542, 622, 700, 780])

A1 = np.array([0.2, 0.71, 1.05, 1.30, 1.57, 1.69, 1.80, 1.88, 2.01, 2.09])
A2 = np.array([2.48, 4.21, 4.75, 4.97, 5.34, 5.32, 5.45, 5.48, 5.64,5.70])
A6 = np.array([ 9.44,11.21 ,11.50, 11.70, 12.12, 12.08, 12.22, 12.22, 12.37, 12.41])
A5 = np.array([2.48, 4.21, 4.75, 4.97, 5.34, 5.32, 5.45, 5.48, 5.64, 5.70])



V1 = np.log(A2 / A1)
V2 = np.log(A6 / A5)
#print(V2)
#print((peaks1 + 1) * 2)
###print(T6[peaks1] - 273.15)
#print((peaks2 + 1) * 2)
###rint(T6[peaks2] - 273.15)
#print(peaks1 * 2  - peaks2 * 2)
###rint(p1 - p2)
##äprint(T1[peaks1] - T1[peaks2])
##print(peaks1 - peaks2)
#print(t2 - t1)
#print(np.mean([26,
#20,
#16,
#16,
#14,
#14,
#14,
#14,
#12,
#12]))
dt1 = unp.uarray([26.00, 20.00, 16.00, 16.00, 14.00, 14.00, 14.00, 14.00, 12.00, 12.00], 0.14)
A1m = unp.uarray([0.20,0.71,1.05,1.30,1.57,1.69,1.80,1.88,2.01,2.09], 0.28)
A2m = unp.uarray([2.48, 4.21, 4.75, 4.97, 5.34, 5.32, 5.45, 5.48, 5.64, 5.70], 0.28)
LNA12 = unp.uarray([2.52, 1.78, 1.51, 1.34, 1.22, 1.15, 1.11, 1.07, 1.03, 1.00], 0.4)
dt5 = unp.uarray([12.00, 8.00, 8.00, 8.00, 8.00, 8.00, 6.00, 6.00, 6.00, 6.00], 0.14)
A5m = unp.uarray([2.48, 4.21, 4.75, 4.97, 5.34, 5.32, 5.45, 5.48, 5.64, 5.70], 0.28)
A6m = unp.uarray([9.44, 11.21, 11.50,11.70,12.12,12.08,12.22,12.22,12.37,12.41], 0.28)
LNA56 = unp.uarray([1.34,0.98,0.88,0.86,0.82,0.82,0.81,0.79,0.80,0.78], 0.4)
kappaA1 = 8520 * 385 * 0.03**2 / (2 * np.mean(dt1) * np.mean(LNA12))
kappaA5 = 2800 * 830 * 0.03**2 / (2 * np.mean(dt5) * np.mean(LNA56))

print(f'meandt1 : {np.mean(dt1)}')
print(f'meandt5 : {np.mean(dt5)}')
print(f'meanLNA12 : {np.mean(LNA12)}')
print(f'meanLNA56 : {np.mean(LNA56)}')
print(f'kappaA1: {kappaA1}')
print(f'kappaA5: {kappaA5}')
print(f'testln : {unp.log(A6m / A5m)}')

