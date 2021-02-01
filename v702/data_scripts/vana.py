#import numpy as np 
#import matplotlib.pyplot as plt
#from uncertainties import ufloat
#Nu = np.mean([129, 143, 144, 136, 139, 126, 158]) #Intervall dt = 300s
#print(Nu)
#Nu /= 10    #Intervall dt = 30s
#
#t, N = np.genfromtxt('data_scripts/Vanadium.dat', unpack = True)
#N -= Nu
##np.savetxt('data_scripts/vana.txt',  np.column_stack([N, np.sqrt(N)]), fmt='%3.2f')
#
#
#params, covariance_matrix = np.polyfit(t, np.log(N/N[0]), deg=1, cov=True)
#errors = np.sqrt(np.diag(covariance_matrix))
#
##print(f'Zerfallskonstante von Vanadium: {params[0]} pm {errors[0]}')
##print(f'Achsenabschnitt von Vanadium: {params[1]} pm {errors[1]}')
#x = np.linspace(t[0], t[-1], 1001)
#
#plt.errorbar(t, N, yerr = np.sqrt(N), fmt = '.', label = 'Messdaten')
#plt.plot(x, N[0] * np.exp(params[1]) * np.exp(params[0] * x ), label = 'Ausgleichsgerade')
#
#plt.xlabel(r'$t \mathbin{/} \si{\second}$')
#plt.ylabel(r'$N$')
#
#plt.yscale('log')
#
#plt.legend()
#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('build/vana.pdf')
#
#lambdaa = ufloat(params[0], errors[0]) 
#
##print(np.log(2) / lambdaa)

#######################

import numpy as np 
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
Nu = np.mean([129, 143, 144, 136, 139, 126, 158]) #Intervall dt = 300s
t, N = np.genfromtxt('data_scripts/Vanadium.dat', unpack = True)

Nerr = np.sqrt(N + Nu)
Nu /= 10

N -= Nu
#np.savetxt('data_scripts/vana.txt',  np.column_stack([N, np.sqrt(N)]), fmt='%3.2f')


params, covariance_matrix = np.polyfit(t, np.log(N), deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print(f'Zerfallskonstante von Vanadium: {params[0]} pm {errors[0]}')
print(f'Achsenabschnitt von Vanadium: {params[1]} pm {errors[1]}')
x = np.linspace(t[0], t[-1], 1001)

plt.errorbar(t, np.log(N), yerr = 0.1 * np.log(Nerr), fmt = '.', label = 'Messdaten')
plt.plot(x, params[0] * x + params[1] , label = 'Ausgleichsgerade')

plt.xlabel(r'$t \mathbin{/} \si{\second}$')
plt.ylabel(r'$N$')

plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/vana.pdf')

lambdaa = ufloat(params[0], errors[0]) 

print(f'Halbwertszeit von Vanadium: {np.log(2) / lambdaa}')