import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat

Nu = np.mean([129, 143, 144, 136, 139, 126, 158]) #Intervall dt = 300s

Nu /= 20    #Intervall dt = 15s
t, N = np.genfromtxt('data_scripts/Rhodium.dat', unpack = True)
tst = np.array([15, 30, 45, 60, 75, 90, 105,120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300])

#np.savetxt('data_scripts/rho.txt', np.column_stack([N - 7, np.sqrt(N-7)]), fmt='%3.2f')
Nerr = np.sqrt(N + Nu)
N -= Nu

plt.errorbar(t, np.log(N), yerr = 0.1 * np.log(Nerr), fmt = '.', label = 'Messdaten')

x0 = np.linspace(t[0], t[-1], 1001)

####################LANGLEBIG#########################
tl, Nl = np.genfromtxt('data_scripts/rhol.dat', unpack = True)
Nl -= Nu

params1, covariance_matrix1 = np.polyfit(tl, np.log(Nl), deg=1, cov=True)
errors1 = np.sqrt(np.diag(covariance_matrix1))

x1 = np.linspace(tl[0], tl[-1], 1000)

#print(Nl[0] *  np.exp( params1[0] * (-300) + params1[1]))

plt.plot(x0,  params1[0] * x0 + params1[1], label = 'Ausgleichsgerade Langlebig')
np.savetxt('data_scripts/rholang.txt', np.column_stack([tl, np.exp( params1[0] * tl + params1[1]), np.sqrt(np.exp( params1[0] * tl + params1[1]))]),fmt='%3.2f')

####################LANGLEBIG#########################
####################KURZLEBIG#########################
 
tk, Nk = np.genfromtxt('data_scripts/rhok.dat', unpack = True)

Nk -= Nu

params0, covariance_matrix0 = np.polyfit(tk, np.log(Nk), deg=1, cov=True)
errors0 = np.sqrt(np.diag(covariance_matrix0))

xk = np.linspace(tk[0], tk[-1], 1000)


Nka = np.exp(params0[0] * tk  + params0[1]) - np.exp(params1[0] * tk + params1[1])

params2, covariance_matrix2 = np.polyfit(tk, np.log(Nka), deg=1, cov=True)
errors2 = np.sqrt(np.diag(covariance_matrix2))

plt.plot(x0, params2[0] * x0 + params2[1], label = 'Ausgleichsgerade kurzlebig')

np.savetxt('data_scripts/rhokurz.txt', np.column_stack([tst, np.exp( params2[0] * tst + params2[1]), np.sqrt(np.exp( params2[0] * tst + params2[1]))]),fmt='%3.2f')

print(f'Zerfallskonstante von Rhodium kurzlebig: {params2[0]} pm {errors2[0]}')
print(f'Achsenabschnitt von Rhodium kurzlebig: {params2[1]} pm {errors2[1]}')

lambdakurz = ufloat(params2[0], errors2[0]) 
print('Halbwertszeit kurzlebig', np.log(2) / lambdakurz)
# ####################KURZLEBIG#########################

plt.xlabel(r'$t \mathbin{/} \si{\second}$')
plt.ylabel(r'$\ln \left ( N \right ) $')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/rho2.pdf')
#print(np.log(np.sqrt(665)))