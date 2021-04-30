import numpy as np 

t, N = np.genfromtxt('Rhodium.dat', unpack = True)
Nu = np.mean([129, 143, 144, 136, 139, 126, 158])

Nu /= 20

N -= Nu

np.savetxt('ele2.txt', N, fmt='%3.2f')