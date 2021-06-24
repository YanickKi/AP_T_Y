import numpy as np 
import matplotlib.pyplot as plt


p, Tl, Tw = np.genfromtxt('data/scripts.txt', unpack = True)

plt.plot(Tw, np.log(p))






plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/copper.pdf')