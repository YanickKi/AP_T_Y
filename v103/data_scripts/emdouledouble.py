from uncertainties import ufloat
import numpy as np


m1r = ufloat(0.002019873863385362,0.0002471363106600821)    # braun rund, 365.1g, 1 * 60.1cm, Gewichtslast von 2355.3g
m1l = ufloat(0.0023272877953585225, 0.00016196839196169554) # braun rund, 365.1g, 1 * 60.1cm, Gewichtslast von 2355.3g
m2r = ufloat(0.0013243883233651894, 0.00010633601905330907) # braun viereckig, 463.7g, 1*1 * 60.1cm  , Gewichtslast von: 2355.3g
m2l = ufloat(0.0013345940720314088, 0.0001008800979353602)  # braun viereckig, 463.7g, 1*1 * 60.1cm  , Gewichtslast von: 2355.3g
m3r = ufloat(0.005233114918186501, 0.0003638354929582845)   # silber viereckig, 166.8g, 1*1*60.1cm  , Gewichtslast von: 2355.3g
m3l = ufloat(0.007063543257233296, 0.000152091293980731)    # silber viereckig, 166.8g, 1*1*60.1cm  , Gewichtslast von: 2355.3g
m4r = ufloat(0.004411053775549133, 0.00033742406265032564)  # rund braun/gelb, 378.5, 1 * 60.1cm , Gewichtslast von:1045.1g
m4l = ufloat(0.004522225509860312, 0.00042685724850456436)  # rund braun/gelb, 378.5, 1 * 60.1cm , Gewichtslast von:1045.1g

mrund = np.array([m1r, m1l, m4r, m4l])
meckig = np.array([m2r, m2l, m3r, m3l])

#Mrund = np.array([0.3651, 0.3651, 0.3785, 0.3785])
#Meckig= np.array([0.4637, 0.4637, 0.1668, 0.1668])

F = 9.81 * 2.3553

Irund = np.pi/64    *1e-8
Ieckig= 1/12        *1e-8

Erund =  F/(48*mrund*Irund)
Eeckig = F/(48*meckig*Ieckig)

print(f'runde Elastizitätsmodule: {Erund}')
print(f'eckige Elastizitätsmodule: {Eeckig}')