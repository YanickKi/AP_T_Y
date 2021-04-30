import numpy as np 

t, N = np.genfromtxt('Vanadium.dat', unpack = True)
Nu = np.mean([129, 143, 144, 136, 139, 126, 158])

Nu /= 10

N -= Nu

np.savetxt('ele.txt', N, fmt='%3.2f')