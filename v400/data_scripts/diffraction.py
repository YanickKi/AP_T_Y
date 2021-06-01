import numpy as np 
from uncertainties import ufloat

gsmall, rsmall, gmiddle, rmiddle, gbig, rbig = np.genfromtxt('diffraction.txt', unpack = True)

def radians(theta):
    return theta/180 * np.pi

def degree(theta):
    return theta/np.pi * 180

def wavelength(d, phi):
    k = 1
    value= np.zeros(6)
    while(k<len(phi)):
            value[k] = d * np.sin(phi[k]) / k 
            k += 1
    return value

d1 = 1e-5
d2 = 1/3*1e-5
d3 = 1/6*1e-5

wgsmall  = wavelength(d1, radians(gsmall))
wrsmall  = wavelength(d1, radians(rsmall)) 
wgmiddle = wavelength(d2, radians(gmiddle))
wrmiddle = wavelength(d2, radians(rmiddle))
wgbig    = wavelength(d3, radians(gbig))
wrbig    = wavelength(d3, radians(rbig))


np.savetxt(
    'diffractio_wavelength.txt',
    np.column_stack([wgsmall*1e9, wrsmall*1e9, wgmiddle*1e9, wrmiddle*1e9, wgbig*1e9, wrbig*1e9]),
    fmt= '%.2f',
)

lambdag = np.array([523.36, 505.28, 504.20, 502.69, 507.52, 492.70, 495.62, 414.43, 512.26])
lambdar = np.array([610.49, 609.35, 607.45, 604.80, 608.07, 584.56, 597.28, 605.15, 610.84])

lambdagerr = ufloat(np.mean(lambdag), np.mean(lambdag) / len(lambdag))
lambdarerr = ufloat(np.mean(lambdar), np.mean(lambdar) / len(lambdar))

print(f'Die Wellenlänge von dem grünen Licht ist gemittelt {lambdagerr:.2f}' )
print(f'Die Wellenlänge von dem roten Licht ist gemittelt {lambdarerr:.2f}' )