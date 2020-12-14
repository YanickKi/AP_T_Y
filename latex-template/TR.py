import numpy as np
from uncertainties import ufloat

cw = np.array([4.1783e3, 4.1783e3, 4.1787e3, 4.1807e3])
cw2= np.array([4.1849e3, 4.1880e3, 4.1922e3, 4.2077e3])
dT1= np.array([0.0164, 0.0145, 0.0125, 0.0067])
dT2= np.array([-0.0101, -0.0095, -0.0089, -0.0072])
N  = np.array([120, 120, 120, 122])
T1 = np.array([32.9, 37.6, 41.4, 50.3])
T2 = np.array([16.2, 13.0, 10.4, 2.9])
p1 = np.array([8.0, 9.0, 10.0, 12.0])
p2 = np.array([4.0, 3.6, 3.4, 3.2])
T1 += 273.15
T2 += 273.15
L = 106.5588
K = 1.14
p1 *= 100000
p2 *= 100000

#rho0 = 5510 # g / m^3
#rho = p2 * rho0 * 273.15 / (100000 * T2e) 

#md = (4 * cw2 + 750 ) * dT2 * (1 / L)
#Nmech = (1 / (K - 1)) * (p1 * (p2 / p1)**(1./1.14) - p2) * md / rho
#µid = T1 / (T1 - T2)
#print(md)

#µ = (4 * cw + 750 ) * dT1 * (1 / N)

#etha = µ / µid
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
t, T1, p1, T2, p2, N=np.genfromtxt('Daten.txt', unpack=True)
T1 = T1 + 273.15
T2 = T2 + 273.15
T1 = 1 / T1
p1 = p1 + 1
p1 = np.log(p1)
xaerr = np.ones(36) * 0.0000032
xa = unp.uarray(T1, xaerr)


params, covariance_matrix = np.polyfit(T1, p1, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

aerr =  ufloat(params[0], errors[0])
berr =  ufloat(params[1], errors[1])

p  = (aerr * xa + berr)
print(p)