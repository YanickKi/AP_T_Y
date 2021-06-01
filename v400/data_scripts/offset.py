import numpy as np 
from uncertainties import ufloat

alpha, beta = np.genfromtxt('refraction.txt', unpack = True)

def radians(theta):
    return theta/180 * np.pi

def degree(theta):
    return theta/np.pi * 180


s = 0.0585 * np.sin(radians(alpha) - radians(beta))/np.cos(radians(beta)) 

np.savetxt(
    'offset_calculated.txt',
    s,
    fmt= '%.4f',
)

serr = ufloat(np.mean(s), np.std(s)/len(s))



n = np.sin(radians(alpha))/np.sin(radians(beta))
nmean = np.mean(n)
nerr = ufloat(np.mean(n), np.std(n)/len(n))

beta = np.arcsin(np.sin(radians(alpha))/nmean)

stilde = 0.0585 * np.sin(radians(alpha) - beta)/np.cos(beta) 
stildeerr = ufloat(np.mean(stilde), np.mean(stilde)/len(stilde))
np.savetxt(
    'offset_index.txt',
    np.column_stack([degree(beta), stilde]),
    fmt= '%.4f',
)


print(f'Der Mittelwert von dem berechneten Strahlenversatz ist {stildeerr:.4f}')
print(f'Der Mittelwert von dem berechneten Strahlenversatz tilde ist {serr:.4f}')