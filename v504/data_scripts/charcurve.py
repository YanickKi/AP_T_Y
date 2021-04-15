import numpy as np
import matplotlib.pyplot as plt    

#alle Ixy in 20mA

U20, I20 = np.genfromtxt('data_scripts/suctionflow20.txt', unpack=True)
U21, I21 = np.genfromtxt('data_scripts/suctionflow21.txt', unpack=True)
U22, I22 = np.genfromtxt('data_scripts/suctionflow22.txt', unpack=True)
U23, I23 = np.genfromtxt('data_scripts/suctionflow23.txt', unpack=True)
U24, I24 = np.genfromtxt('data_scripts/suctionflow24.txt', unpack=True)
U25, I25 = np.genfromtxt('data_scripts/suctionflow25.txt', unpack=True)

#alle Ixy in mA

I20 *=20
I21 *=20
I22 *=20
I23 *=20
I24 *=20
I25 *=20


plt.plot(U22, I22,'.', label = r'$I_{\text{A}1}  \; ( I_\text{H} = \SI{2.0}{\ampere} \text{,} \; U_\text{H} = \SI{4.0}  {\volt})   $')
plt.plot(U21, I21,'.', label = r'$I_{\text{A}2}  \; ( I_\text{H} = \SI{2.1}{\ampere} \text{,} \; U_\text{H} = \SI{4.1}{\volt})     $')
plt.plot(U20, I20,'.', label = r'$I_{\text{A}3}  \; ( I_\text{H} = \SI{2.2}{\ampere} \text{,} \; U_\text{H} = \SI{4.2}{\volt})     $')
plt.plot(U23, I23,'.', label = r'$I_{\text{A}4}  \; ( I_\text{H} = \SI{2.3}{\ampere} \text{,} \; U_\text{H} = \SI{4.7}{\volt})     $')
plt.plot(U24, I24,'.', label = r'$I_{\text{A}5}  \; ( I_\text{H} = \SI{2.4}{\ampere} \text{,} \; U_\text{H} = \SI{5.0}  {\volt})   $')
plt.plot(U25, I25,'.', label = r'$I_{\text{A}6}  \; ( I_\text{H} = \SI{2.5}{\ampere} \text{,} \; U_\text{H} = \SI{5.3}{\volt})     $')

plt.xlabel(r'$ U \mathbin{/} \si{\volt}$')
plt.ylabel(r'$ I_{\text{A}} \mathbin{/} \si{\milli\ampere}$')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.legend()
plt.savefig('build/charcurve.pdf')