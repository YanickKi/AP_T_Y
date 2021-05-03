import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unp
import matplotlib.pyplot as plt

alpha = ufloat(7.2973525693e-3, 11e-9)

def energie(theta):
    return 6.626e-34 * 299792458 / (2 * 201.4e-12 * np.sin(theta) * 1.602e-19) 

def radians(theta):
    return theta/180 * np.pi

def constant(z, energie):
    return z - unp.sqrt(energie/13.6 - alpha**2 * z**4/ 4)


z = [30, 31, 35, 37, 38, 40]
Ezink       = energie(radians(18.75)) 
Egallium    = energie(radians(17.35))
Ebrom       = energie(radians(13.25))
Erubidium   = energie(radians(11.75))
Estrontium  = energie(radians(11.05))
Ezirkonium  = energie(radians(9.95))
constantzink       = constant(z[0], Ezink) 
constantgallium    = constant(z[1], Egallium)
constantbrom       = constant(z[2], Ebrom)
constantrubidium   = constant(z[3], Erubidium)
constantstrontium  = constant(z[4], Estrontium)
constantzirkonium  = constant(z[5], Ezirkonium) 
print(f'Abschirmenergie von Zink        = {Ezink}')
print(f'Abschirmenergie von Gallium     = {Egallium}')
print(f'Abschirmenergie von Brom        = {Ebrom}')
print(f'Abschirmenergie von Rubidium    = {Erubidium}')
print(f'Abschirmenergie von Strontium   = {Estrontium}')
print(f'Abschirmenergie von Zirkonium   = {Ezirkonium}')
print(f'Abschirmkonstante von Zink      = {constantzink     :.4f}')
print(f'Abschirmkonstante von Gallium   = {constantgallium  :.4f}')
print(f'Abschirmkonstante von Brom      = {constantbrom     :.4f}')
print(f'Abschirmkonstante von Rubidium  = {constantrubidium :.4f}')
print(f'Abschirmkonstante von Strontium = {constantstrontium:.4f}')
print(f'Abschirmkonstante von Zirkonium = {constantzirkonium:.4f}')

Energies = np.array([Ezink, Egallium, Ebrom, Erubidium, Estrontium, Ezirkonium])
Constants = np.array([constantzink, constantgallium, constantbrom, constantrubidium, constantstrontium, constantzirkonium])


params, covariance_matrix = np.polyfit(z, np.sqrt(Energies), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

x = np.linspace(z[0], z[-1])

plt.plot(z, np.sqrt(Energies), '.', label = 'Daten')
plt.plot(x, params[0] * x + params[1], label = 'Regressionsgerade')

plt.xlabel(r'$Z$')
plt.ylabel(r'$\sqrt{E_K} \mathbin{/} \sqrt{\si{\electronvolt}}$')

m = ufloat(params[0], errors[0])

R = m**2 * 1.602e-19 / 6.626e-34

Renergie = 6.626e-34 * R /  1.602e-19

print(f'Regressionsparameter m = {params[0]} pm {errors[0]}')
print(f'Regressionsparameter b = {params[1]} pm {errors[1]}')
print(f'Rydbergfrequenz = {R}')
print(f'Rydbergenergie = {Renergie}')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/rydberg.pdf')

litconstant = np.array([3.566, 3.677, 3.848, 3.944, 3.999, 4.101])
eta = Constants / litconstant * 100

print(eta)
