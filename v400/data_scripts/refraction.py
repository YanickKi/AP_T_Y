import numpy as np 
from uncertainties import ufloat

alpha, beta = np.genfromtxt('refraction.txt', unpack = True)

def radians(theta):
    return theta/180 * np.pi


n = np.sin(radians(alpha))/np.sin(radians(beta))

np.savetxt(
    'refractionsindex_plexi.txt',
    n,
    fmt= '%.4f',
)

nerr = ufloat(np.mean(n), np.std(n)/len(n))

c = 2.9979e8 / nerr

print(f'Der Mittelwert von dem berechneten Brechungsindex ist {np.mean(n)} pm {np.std(n)/len(n)}')
print(f'Die Lichtgeschwindigkeit in Plexiglas ist{c}')