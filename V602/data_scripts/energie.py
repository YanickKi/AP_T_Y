import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp

alpha = ufloat(7.2973525693e-3, 11e-9)

def energie(theta):
    return 6.626e-34 * 299792458 / (2 * 201.4e-12 * np.sin(theta) * 1.602e-19) 

def radians(theta):
    return theta/180 * np.pi

def constant(energie):
    return 29 - unp.sqrt(energie/13.6 - alpha**2 * 29**4/ 4)

Ezink       = energie(radians(18.75)) 
Egallium    = energie(radians(17.35))
Ebrom       = energie(radians(13.25))
Erubidium   = energie(radians(11.75))
Estrontium  = energie(radians(11.05))
Ezirkonium  = energie(radians(9.95))
constantzink       = constant(Ezink) 
constantgallium    = constant(Egallium)
constantbrom       = constant(Ebrom)
constantrubidium   = constant(Erubidium)
constantstrontium  = constant(Estrontium)
constantzirkonium  = constant(Ezirkonium)

print(f'Abschirmenergie von Zink        = {Ezink}')
print(f'Abschirmenergie von Gallium     = {Egallium}')
print(f'Abschirmenergie von Brom        = {Ebrom}')
print(f'Abschirmenergie von Rubidium    = {Erubidium}')
print(f'Abschirmenergie von Strontium   = {Estrontium}')
print(f'Abschirmenergie von Zirkonium   = {Ezirkonium}')
print(f'Abschirmkonstante von Zink      = {constantzink:.2f}')
print(f'Abschirmkonstante von Gallium   = {constantgallium:.2f}')
print(f'Abschirmkonstante von Brom      = {constantbrom:.2f}')
print(f'Abschirmkonstante von Rubidium  = {constantrubidium:.2f}')
print(f'Abschirmkonstante von Strontium = {constantstrontium:.2f}')
print(f'Abschirmkonstante von Zirkonium = {constantzirkonium:.2f}')