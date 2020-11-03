import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
t, T1, p1, T2, p2, N=np.genfromtxt('Daten.txt', unpack=True)
T1 = T1 + 273.15
T2 = T2 + 273.15
T1 = 1 / T1
p1 = p1 + 1
p1 = np.log(p1)
params, covariance_matrix = np.polyfit(T1, p1, deg=1, cov=True)
perr = np.array([0.32972842530040436, 0.3289671600974837, 0.3282141231683453, 0.32764038941841056, 0.32701476296869425, 0.32639481141209514, 0.3256693650775238, 0.32517166262306435, 0.32451375376996044, 0.323970412384939, 0.3234314888825514, 0.3228969359388119, 0.32241953651507443, 0.3219456058127679, 0.3214230440288903, 0.3209563276357834, 0.3205442960062151, 0.3201349020243174, 0.3197281234500054, 0.3193743203439949, 0.3190224882114004, 0.3186227892362297, 0.31827513208851776, 0.3179294009060545, 0.31758558163856615, 0.3172923905808556, 0.31700058527162456, 0.3167101570854512,0.316421097464015, 0.31613339791546374, 0.3158946811553218, 0.3156094532365841, 0.31537278449168693, 0.31513703900589973, 0.3149022120367003, 0.314715008625746])






errors = np.sqrt(np.diag(covariance_matrix))

#for name, value, error in zip('abc', params, errors):
#    print(f'{name} = {value} ± {error}')
xaerr = np.ones(36) * 0.0000032
xa = unp.uarray(T1, xaerr)

aerr = ufloat(params[0], errors[0])
Rerr = ufloat(-8.314462, 0.0)
Lerr = Rerr * aerr
berr =  ufloat(params[1], errors[1])
p  = (aerr * xa + berr)
x = np.linspace(T1[0], T1[-1], 100)
plt.errorbar(T1, p1, xerr = 0.0000032, yerr = perr, fmt = '.', label = 'Daten')                                                                                        
plt.plot(x, params[0] * x + params[1], label = 'Ausgleichsgerade')                                    
plt.xlabel(r'$\frac{1}{T} \:/\: \si{\kelvin\tothe{-1}}$')
plt.ylabel(r'$\ln (p)')
plt.legend(loc='best')
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/Verdampfungswaerme.pdf')