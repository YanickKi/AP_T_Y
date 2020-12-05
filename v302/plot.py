import numpy as np
import matplotlib.pyplot as plt    

w,UB=np.genfromtxt('dataplots/WR_data.txt', unpack=True)
US=5000
w0=162.56
print(w)
print(UB/US)
om=w/w0

plt.plot(om,UB/US,'r--', label= '$U_{Br} \mathbin{/} U_S')
f=np.sqrt(1/9*(om**2-1)**2/((1-om**2)**2+9*om**2))

plt.plot(om,f, label='$f(\symup{\Omega})$')
plt.legend()
plt.xscale('log')
plt.ylabel('Y')
plt.xlabel('$Frequenz \mathbin{/} \Omega$')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
