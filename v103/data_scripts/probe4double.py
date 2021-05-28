import numpy as np 
import matplotlib.pyplot as plt

xr, xl, Dr, Dl = np.genfromtxt('data_scripts/probe4double.txt', unpack = True)

xr *= 1e-2
xl *= 1e-2
Dr *= 1e-3
Dl *= 1e-3

linearright = 3*0.601**2*xr - 4*xr**3
linearleft  = 4*xl**3 - 12*0.601*xl**2 + 9 * 0.601**2*xl - 0.601**3

params1, covariance_matrix1 = np.polyfit(linearright, Dr, deg=1, cov=True)
errors1 = np.sqrt(np.diag(covariance_matrix1))

params2, covariance_matrix2 = np.polyfit(linearleft, Dl, deg=1, cov=True)
errors2 = np.sqrt(np.diag(covariance_matrix2))

x_plotright = np.linspace(linearright[0], linearright[-1], 1000)
x_plotleft = np.linspace(linearleft[0], linearleft[-1], 1000)

plt.subplot(1, 2, 1)
plt.plot(linearright, Dr*1e3, '.', label = 'Messwerte')
plt.plot(x_plotright, (params1[0] * x_plotright + params1[1]) * 1e3, label = 'Regressionsgerade')
plt.xlabel(r'$3L^2x-4x^3 \mathbin{/} \si{\metre}$')
plt.ylabel(r'$D \mathbin{/} \si{\milli\metre}$')
plt.title(r"$0 \leq x \leq \sfrac{L}{2} $")
plt.ylim(-0.001, 0.83)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(linearleft, Dl*1e3, '.', label = 'Messwerte')
plt.plot(x_plotleft, (params2[0] * x_plotleft + params2[1]) * 1e3, label = 'Regressionsgerade')
plt.xlabel(r'$4x^3-12Lx^2+9L^2x-L^3  \mathbin{/} \si{\metre}$')
plt.title(r"$\sfrac{L}{2} \leq x \leq L $")
plt.ylim(-0.001, 0.83)
plt.legend()

print(f'der Paremter m von der Probe4 rechts ist = {params1[0]} pm {errors1[0]}')
print(f'der Paremter b von der Probe4 rechts ist = {params1[1]} pm {errors1[1]}')
print(f'der Paremter m von der Probe4 links  ist = {params2[0]} pm {errors2[0]}')
print(f'der Paremter b von der Probe4 links  ist = {params2[1]} pm {errors2[1]}')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/probe4double.pdf')