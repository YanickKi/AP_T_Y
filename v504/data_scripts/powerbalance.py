import numpy as np
#data_scripts


U = np.array([4.0, 4.1, 4.2, 4.7, 5.0, 5.3])
I = np.array([2.0, 2.1, 2.2, 2.3, 2.4, 2.5])

T = ((U * I - 1) / (0.32 * 0.28 * 5.7 * 10**(-12)))**(1/4)
 
Is = np.array([2.2, 5.4, 12.6, 25.8, 50, 80])
Is = np.array([0.11, 0.27, 0.63, 1.29, 2.5, 4])

Is *= 1e-3

W = 1.380649e-23 * T * np.log(38.2*T**2/Is) / (1.602*1e-19)

Is *= 1e3

print(np.mean(W))
print(np.std(W, ddof=1) / np.sqrt(len(W)))

np.savetxt('workfunction.txt', np.column_stack([U, I, T, Is, W]), fmt='%4.2f')