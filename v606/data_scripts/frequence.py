import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat


w, UE = np.genfromtxt('data_scripts/frequence.txt', unpack = True)

UE /= 10 #Verstärkung rausnehmen
U =  UE/0.01


def f(x, x0, a, gamma):
    return a / ((x**2 -x0**2)**2 + gamma**2*x0**2)

params, covariance_matrix = curve_fit(f, w, U)
errors = np.sqrt(np.diag(covariance_matrix))


print(params[0], params[1], params[2])

x = np.linspace(w[0], w[-1], 1000)
 

curve = f(x, *params)
print(max(curve))

k = 0
i = 0
while(k < 1000):
    if(curve[k] >= max(curve)/np.sqrt(2)):
        print(f'w- ist  {x[k-1]}')
        wminus = x[k-1]
        i = k
        k = 1000
    k +=1

while(i < 1000):
    if(curve[i] <= max(curve)/np.sqrt(2)):
        print(f'w+ ist  {x[i]}')
        wplus = x[i]
        i = 1000
    i +=1

nu0 = ufloat(params[0], errors[0])

print(f'Die experimentelle Güte beträgt {nu0/(wplus - wminus)}')


print(f'Der Paramter x0 ist {params[0]} pm {errors[0]}')
print(f'Der Paramter a ist {params[1]} pm {errors[1]}')
print(f'Der Paramter gamma ist {params[2]} pm {errors[2]}')

plt.plot(w, U, '.', label = 'Messwerte')
#plt.plot(x, f(x, *params), label = 'Regressionskurve')
#plt.hlines(xmin = x[0], xmax = x[-1], y = max(curve)/np.sqrt(2), label = r'$\sfrac{U_\text{max}}{\sqrt{2}}$', color = 'tab:green')


plt.xlabel(r'$\nu \mathbin{/} \si{\kilo\hertz}$')
plt.ylabel(r'$U_\text{A}U_\text{E}^{-1}$')
plt.legend()

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/frequence.pdf')