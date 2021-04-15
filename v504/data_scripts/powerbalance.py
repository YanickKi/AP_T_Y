import numpy as np
#data_scripts


U = np.array([4.0, 4.1, 4.2, 4.7, 5.0, 5.3])
I = np.array([2.0, 2.1, 2.2, 2.3, 2.4, 2.5])

T = ((U * I - 1) / (0.32 * 0.28 * 5.7 * 10**(-12)))**(1/4)
 
Is = np.array([2.2, 5.4, 12.6, 25.8, 0.00001, 0.000001])

Is /= 1e-3


W = - 1.380649e-23 * T * np.log(Is * (6.62607015e-34)**3 / ( 4 * np.pi * 1.602e-19 * 9.109e-31 * (1.380649e-23)**2 * T**2 * 0.32e-4)) / (1.602e-19)

Is *= 1e-3


index = [-1, -2]
W = np.delete(W, index)
print(np.mean(W))
print(np.std(W, ddof=1) / np.sqrt(len(W)))



np.savetxt('workfunction.txt', np.column_stack([U, I, T, Is, W]), fmt='%4.2f')