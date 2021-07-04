import numpy as np 

T = np.array([26, 140, 165, 175]) + 273.15

p = 5.5e7 * np.exp(-6876/T) 
w = 0.0029/p * 1e-2

V = 1e-2/w


np.savetxt(
    'ratio.txt',
    np.column_stack([T, p, w , V]),    
)

print(f'Die Anregungsenergie beträgt {5 * 1.602e-19}')

print(f'Die Wellenlänge der Photonen ist {299792458 * 6.62607015e-34 / (5*1.602e-19)}')