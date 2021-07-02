import numpy as np 
from uncertainties import ufloat

l1 = ufloat(52.19e-12, 1.25e-12)

l2 = ufloat(55.95e-12, 1.29e-12)
l3 = l2 - l1

l3 *= 1e12

print(f'{l3:.2f}')