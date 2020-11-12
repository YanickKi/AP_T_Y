import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t, T1, T4, T5, T8, T2, T3, T6, T7 = np.genfromtxt('dynamisch40.txt', unpack = True)
T1 += 273.15
T2 += 273.15
T3 += 273.15
T4 += 273.15
T5 += 273.15
T6 += 273.15
T7 += 273.15
T8 += 273.15

def f1(s, A, w, k):
    return A * np.exp(-np.sqrt(w * 8520 * 0.385 / (2 * k)) * 0.03) * np.cos(w * s - np.sqrt(w * 8520 * 0.385 / (2 * k)) * 0.03)

def f2(s, A, w):
    return A * np.cos(w * s)

params1, pcov1 = curve_fit(f1, t, T1)
params2, pcov2 = curve_fit(f2, t, T1)
params = np.sqrt(params1**2)
params = np.sqrt(params2**2)
µ = np.linspace(0, 420, 420)

plt.plot(t, f1(µ, params1[0], params1[1], params1[2]))
plt.plot(t, f2(µ, params2[0], params2[1]))
plt.plot(t*2, T1, label = 'T1')
plt.plot(t*2, T2, label = 'T2')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('Me.pdf')