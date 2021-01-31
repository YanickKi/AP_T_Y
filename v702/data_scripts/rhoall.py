import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat
Nu = np.mean([129, 143, 144, 136, 139, 126, 158]) #Intervall dt = 300s
Nu /= 20    #Intervall dt = 15s
t, N = np.genfromtxt('data_scripts/Rhodium.dat', unpack = True)
#np.savetxt('data_scripts/rho.txt', np.column_stack([N - 7, np.sqrt(N-7)]), fmt='%3.2f')
N -= Nu

params0, covariance_matrix0 = np.polyfit(t, np.log(N/N[0]), deg=1, cov=True)
errors0 = np.sqrt(np.diag(covariance_matrix0))

x0 = np.linspace(t[0], t[-1], 1000)

plt.plot(x0,  N[0] *  np.exp( params0[0] * x0 + params0[1] ), label = 'Ausgleichsgerade Gesamt')

print(f'Zerfallskonstante von Rhodium Gesamt: {params0[0]} pm {errors0[0]}')
print(f'Achsenabschnitt von Rhodium Gesamt: {params0[1]} pm {errors0[1]}')

####################LANGLEBIG#########################

tl, Nl = np.genfromtxt('data_scripts/rhol.dat', unpack = True)
Nl -= Nu

params1, covariance_matrix1 = np.polyfit(tl, np.log(Nl/Nl[0]), deg=1, cov=True)
errors1 = np.sqrt(np.diag(covariance_matrix1))

print(f'Zerfallskonstante von Rhodium langlebig: {params1[0]} pm {errors1[0]}')
print(f'Achsenabschnitt von Rhodium langlebig: {params1[1]} pm {errors1[1]}')

x1 = np.linspace(tl[0], tl[-1], 1000)

plt.plot(x0,  N[0] *  np.exp( params1[0] * x0 + params1[1] ), label = 'Ausgleichsgerade Langlebig')

####################LANGLEBIG#########################

####################KURZLEBIG#########################

tk = np.genfromtxt('data_scripts/rhok.dat')

xk = np.linspace(tk[0], tk[-1],1000)

Nk = N[0] *  np.exp( params0[0] * tk + params0[1]) - N[0] *  np.exp( params1[0] * tk + params1[1])

params2, covariance_matrix2 = np.polyfit(tk, np.log(Nk/Nk[0]), deg=1, cov=True)
errors2 = np.sqrt(np.diag(covariance_matrix2))

xk = np.linspace(tk[0], tk[-1], 1000)

plt.plot(x0,  N[0] *  np.exp( params2[0] * x0 + params2[1] ), label = 'Ausgleichsgerade Kurzlebig')

####################KURZLEBIG#########################

plt.xlabel(r'$t \mathbin{/} \si{\second}$')
plt.ylabel(r'$N$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/rhoall.pdf')

#lambdaa = ufloat(params[0], errors[0]) 
#
#print(np.log(2) / lambdaa)

np.savetxt('rhofuck.txt', [N[0] *  np.exp( params1[0] * t + params1[1]) + N[0] *  np.exp( params2[0] * t + params2[1])], fmt='%3.0f')