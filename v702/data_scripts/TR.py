import numpy as np 

t, N = np.genfromtxt('Vanadium.dat', unpack = True)
N -= 14

np.savetxt('test.txt', np.sqrt(N))