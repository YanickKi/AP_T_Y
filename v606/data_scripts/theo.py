import numpy as np 

µ0 = 1.25663706212e-6
µB = 9.2740100783e-24 
NA = 6.02214076e23
T  = 293.15
kB = 1.380649e-23
L  = np.array([5, 6])
S  = np.array([5/2, -3/2])
J  = L + S
gj = (3*J*(J+1) + (S*(S+1)-L*(L+1))) / (2*J*(J+1))
rho= np.array([7.8, 7.24]) * 1e3
M  = np.array([372.998, 336.48]) * 1e-3

N = 2 * rho/M * NA

chi = µ0*µB**2*gj**2*N*J*(J+1)/(3*kB*T)

print(J)
print(gj)
print(N)
print(chi)