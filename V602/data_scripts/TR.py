import numpy as np 
from uncertainties import ufloat
import uncertainties.unumpy as unp

def energie(theta):
    return 6.626e-34 * 299792458 / (2 * 201.4e-12 * unp.sin(theta))
 
def radians(theta):
    return theta/180 * np.pi

thetaerr = unp.uarray([20.2, 22.5, 22.35537, 22.84919, 20.55552, 20.06083], 4.9362)

ka = energie(radians(thetaerr[1]))                                    / 1.602e-19
kb = energie(radians(thetaerr[0]))                                    / 1.602e-19
dka= (energie(radians(thetaerr[3])) - energie(radians(thetaerr[2])))  / 1.602e-19    
dkb= (energie(radians(thetaerr[4])) - energie(radians(thetaerr[5])))  / 1.602e-19

print(f'Kalpha Energie:{ka:.2f}')
print(f'Kbeta Energie :{kb:.2f}')
print(f'dKalpha:{dka:.2f} ')
print(f'dKbeta :{dkb:.2f} ')
print(f'Auflösevermögen ka: {ka/dka:.2f}')
print(f'Auflösevermögen kb: {kb/dkb:.2f}')

print(f'Delta Theta k alpha = {thetaerr[3] - thetaerr[2]:.4f}')
print(f'Delta Theta k alpha = {thetaerr[4] - thetaerr[5]:.4f}')

Eabs = ufloat(8987.96, 15)
Ealpha = 8.04e3
Ebeta  = 8.92e3 
sigma1 = 29 - unp.sqrt(Eabs/ 13.6)
sigma2 = 29 - 2 * unp.sqrt((13.6 * (29 - sigma1)**2 - Ealpha) / 13.6)
sigma3 = 29 - 3 * unp.sqrt((29 - sigma1)**2 - Ebeta / 13.6 )
print(f'Sigma 1 = {sigma1:.2f}')
print(f'sigma 2 = {sigma2:.2f}')
print(f'sigma 3 = {sigma3:.2f}')