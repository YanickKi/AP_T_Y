import numpy as np 
from uncertainties import ufloat

alpha1, alpha2green, alpha2red = np.genfromtxt('prisma.txt', unpack = True)

def radians(theta):
    return theta/180 * np.pi

def degree(theta):
    return theta/np.pi * 180

def beta1(alpha1):
    return np.arcsin(np.sin(alpha1)/1.555)

def beta2(beta1):
    return radians(60) - beta1

def delta(alpha1, alpha2, beta1, beta2):
    return alpha1 + alpha2 - beta1 - beta2

alpha1 = radians(alpha1)
alpha2green = radians(alpha2green)
alpha2red = radians(alpha2red)

beta1green  = beta1(alpha1)
beta1red    = beta1(alpha1)
beta2green  = beta2(beta1green)
beta2red    = beta2(beta1red)
deltagreen  = delta(alpha1, alpha2green, beta1green, beta2green) 
deltared    = delta(alpha1, alpha2red, beta1red, beta2red) 

np.savetxt(
    'deflection.txt',
    np.column_stack([degree(deltagreen), degree(deltared)]),
    fmt= '%.4f',
)