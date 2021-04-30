import numpy as np

d, I = np.genfromtxt('distance.txt', unpack = True)

dh = d / 5.046 

index = [2, 4]
dh = np.delete(dh, index)
I = np.delete(I, index)
#wl = 2 * dh / (I * 1e3)  #wl in m

wl = 2 * np.mean(dh) / (np.mean(I) * 1e3)  #wl in m

wl *= 1e9       #wl in nm
print(wl)
#np.savetxt('wavelength.txt', np.column_stack([d, dh, I , wl]), fmt='%10.2f')
#
#print(f'error of the entries: {np.std(wl)}')
#index = [2, 4]
#wl = np.delete(wl, index)   #delete Wavelenghts with too high deviation
#
#
#print(f'Average wavelength of the light source: {np.mean(wl)}')
#print(f'error of the average wavelength: {np.std(wl, ddof=1) / np.sqrt(len(wl))}')