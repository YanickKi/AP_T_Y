import numpy as np

C2,R2,R3,R4=np.genfromtxt('datac1.txt', unpack=True)

Rx=R2*R3/R4
print(Rx)
Cx=C2*R4/R3
print(Cx)