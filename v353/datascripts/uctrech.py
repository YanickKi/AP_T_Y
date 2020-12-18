import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat

t, U = np.genfromtxt('uct.txt', unpack = True)
U       += 3.1
t       *= 0.2

print(f' t = {t} in ms')
print(f' U = {U} in V')

