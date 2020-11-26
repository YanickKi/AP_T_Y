import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from scipy.signal import find_peaks
from uncertainties import ufloat

#111111111111111111111111111111111111111111111111111111
A1 = unp.uarray([0.10, 0.35, 0.53, 0.65, 0.78, 0.85, 0.90, 0.94, 1.01, 1.04], 0.28)
A2 = unp.uarray([1.24, 2.11, 2.34, 2.49, 2.67, 2.66, 2.73, 2.74, 2.82, 2.85], 0.28)
dt1= unp.uarray([26.00, 20.00, 16.00, 16.00, 14.00, 14.00, 14.00, 14.00, 12.00, 12.00], 0.14) 
rho1 = 8520
c1 = 385

#555555555555555555555555555555555555555555555555555555
A5 = unp.uarray([1.24, 2.11, 2.38, 2.49, 2.67, 2.66, 2.73, 2.74, 2.82, 2.85], 0.28)
A6 = unp.uarray([4.72, 5.61, 5.75, 5.85, 6.61, 6.04, 6.11, 6.11, 6.19, 6.21], 0.28)
dt5= unp.uarray([12.00, 8.00, 8.00, 8.00, 8.00, 8.00, 6.00, 6.00, 6.00, 6.00], 0.14)
rho5= 2800
c5 = 830

#777777777777777777777777777777777777777777777777777777
A7 = unp.uarray([7.23, 7.90, 7.47, 8.66], 0.28)
A8 = unp.uarray([0.03, 0.13, 0.27, 0.43], 0.28)
dt7 = unp.uarray([80, 72, 56, 60], 0.14)
rho7 = 8000
c7 = 400

kappa1 = rho1 * c1 * 0.03**2 / (2 * dt1 * unp.log(A2 / A1))
kappa5 = rho5 * c5 * 0.03**2 / (2 * dt5 * unp.log(A6 / A5))
kappa7 = rho7 * c7 * 0.03**2 / (2 * dt7 * unp.log(A7 / A8))



tau80 = ufloat(80, 0.1)
f80 = 1 / tau80
tau200 = ufloat(200, 0.1)
f200 = 1 / tau200
kappame = unp.uarray(   [ 22.5495, 41.0822, 62.1238, 68.6903, 85.6819, 92.4183, 95.0154, 98.5527, 119.7985,122.0194], 
                        [ 25.1596, 18.5464, 22.6669, 22.7777, 26.0541, 28.0298, 28.0654, 29.0265, 34.3854, 34.7186 ])
kappaalu= unp.uarray(   [ 65.1980, 133.6844, 148.1976, 153.0453, 144.2077, 159.4056, 216.3537, 217.3401, 221.6998, 223.7938],
                        [11.4129, 19.5231, 21.5482, 22.0601, 18.1684, 22.5306, 30.5878, 30.7722, 31.1995, 31.4970])
kappast = unp.uarray(   [3.2818, 4.8696, 7.7447, 7.9928],
                        [5.5846, 2.5541, 2.4206, 1.7356])


lambda1 = unp.sqrt(4 * np.mean(kappast) * np.pi * f200/ (rho7 * c7)) / f200

print(np.mean(kappa5))
print(f200)



print(lambda1)
#print(f'kappa1 : {kappa1} ')
#print(f'kappa5 : {kappa5} ')
#print(f'kappa7 : {kappa7} ')
#print(np.mean(kappast))

#print (1 / tau)