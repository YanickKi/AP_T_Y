import matplotlib.pyplot as plt
import numpy as np

t, T_1=np.genfromtxt('data.txt',)
plt.plot(t,T_1)
plt.show()
