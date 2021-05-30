import numpy as np 

exp = np.array([3.611, 3.668, 3.835, 4.067, 4.109, 4.296])
theo = np.array([3.566, 3.677, 3.848, 3.944, 3.999, 4.101])

def abweichung(exp, theo):
    return abs(theo-exp)/theo*100

print(abweichung(exp, theo))