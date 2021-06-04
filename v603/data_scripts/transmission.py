import numpy as np 
import matplotlib.pyplot as plt 
from uncertainties import ufloat

theta, Nohne = np.genfromtxt('data_scripts/ComptonOhne.txt', unpack = True)
theta, Nmit = np.genfromtxt('data_scripts/ComptonAl.txt', unpack = True)


def energie(theta):
    return 6.626e-34 * 299792458 / (2 * 201.4e-12 * np.sin(theta) * 1.602e-19) 

def radians(theta):
    return theta/180 * np.pi

def correction(N):
    return N/(1-90e-6*N)

def wavelength(theta):
    return 2 * 201.4e-12 * np.sin(radians(theta))

def uncI(N):
    return abs((1/N * correction(N) + 9e-5/N * correction(N)**2)*np.sqrt(N))

def uncT(Nohne, Nmit, Nerrohne, Nerrmit):
    return np.sqrt((1/Nohne * Nerrohne)**2 +  (Nmit/Nohne**2 * Nerrmit)**2) 

Nohneerr= uncI(Nohne)
Nmiterr = uncI(Nmit)
Nohne = correction(Nohne) 
Nmit = correction(Nmit)

Terr = uncT(Nohne, Nmit, Nohneerr, Nmiterr)
T = Nmit/Nohne

np.savetxt(
    'Transmisson.txt',
    np.column_stack([T, Terr]),
    fmt=['%.2f', '%.2f'],    
    header='T,Terr',
)

wavelength = wavelength(theta)

x = np.linspace(wavelength[0], wavelength[-1]) 

params, covariance_matrix = np.polyfit(wavelength, T, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

plt.errorbar(x=wavelength*1e12, y=T, fmt='.', yerr = Terr,  label = 'Transmission')
plt.plot(x*1e12, params[0] * x + params[1], label = 'Regressionsgerade')
plt.xlabel(r'$\lambda \mathbin{/} \si{\pico\meter}$')
plt.ylabel(r'$T$')
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/transmission.pdf')

I0= 2731
I1= 1180
I2= 1024

m = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

T1 = I1/I0
T2 = I2/I0
wavelength1 = (T1 - b)/m
wavelength2 = (T2 - b)/m
print(f'Der Parameter m beträgt {m} ')
print(f'Der Parameter b beträgt {b}')
print(f'Die Transmission T1 beträgt {T1}')
print(f'Die Transmission T2 beträgt {T2}')
print(f'Die Wellänge zu T1 beträgt {wavelength1*1e12:.2f}')
print(f'Die Wellänge zu T2 beträgt {wavelength2*1e12:.2f}')
print(f'Die Compton Wellenlänge beträgt {(wavelength2 - wavelength1)*1e12:.2f}')