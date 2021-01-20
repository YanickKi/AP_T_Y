import numpy as np
from uncertainties import ufloat
N1 = 96041.0 / 120.0
N2 = 76518.0 / 120.0
N21 = 158479.0 / 120.0

n1 =  ufloat(N1, np.sqrt(N1))
n2 =  ufloat(N2, np.sqrt(N2))
n12 = ufloat(N21, np.sqrt(N21))

T = (n1 + n2 - n12) / (2 * n1 * n2)

print(f'Totzeit T = {T}')