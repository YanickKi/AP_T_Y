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

def f(s, A, w, k, x):
    return A * np.exp(-np.sqrt(w * 8520 * 0.385 / (2 * k)) * x) * np.cos(w * s - np.sqrt(w * 8520 * 0.385 / (2 * k)) * x)


params1, pcov1 = curve_fit(f, t * 2, T1, p0 = (40, 0.05 * np.pi, 120, 0.03))
params2, pcov2 = curve_fit(f, t * 2, T2)
µ = np.linspace(0, 420, 420)

print(params1)

plt.plot(µ * 2, f(µ * 2, *params1), label = 'T1fit')
plt.plot(µ * 2, f(µ * 2, *params2), label = 'T2fit')
plt.plot(t*2, T1, label = 'T1')
plt.plot(t*2, T2, label = 'T2')
plt.legend()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('fitWellengleichung.pdf')