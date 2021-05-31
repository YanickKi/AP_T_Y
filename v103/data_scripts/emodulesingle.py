from uncertainties import ufloat
import numpy as np

m1 = ufloat(0.013744952649390893, 0.0021854412872838974) # braun rund, 365.1g, 1 * 60.1cm  , Gewichtslast von:1045.1g
m2 = ufloat(0.026918264335113427, 0.0007414372788670032) # braun viereckig, 463.7g, 1*1 * 60.1cm  , Gewichtslast von:1045.1g
m3 = ufloat(0.06804939315843149 , 0.0025712099438414435) # silber viereckig, 166.8g, 1*1*60.1cm  , Gewichtslast von:1045.1g
m4 = ufloat(0.0686618330681571  , 0.0038252793921409213) # rund braun/gelb, 378.5, 1 * 60.1cm , Gewichtslast von:1045.1g

mrund = np.array([m1, m4])
meckig = np.array([m2, m3])

F = 9.81 * 1.0451

Irund = np.pi/64    *1e-8
Ieckig= 1/12        *1e-8

Erund =  F/(2*mrund*Irund)
Eeckig = F/(2*meckig*Ieckig)

print(f'runde Elastizitätsmodule: {Erund}')
print(f'eckige Elastizitätsmodule: {Eeckig}')
