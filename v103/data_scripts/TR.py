import numpy as np 

ein = np.array([759.77, 228.52, 90.4, 152.09])
zweirechts = np.array([485.49, 436.15, 110.04, 222.31])
zweilinks = np.array([421.36, 432.82, 81.78, 216.84])

lit = np.array([1000000000, 205, 70, 123])

abweichungeins = abs(lit -ein ) / lit * 100
abweichungrechts = abs(lit -zweirechts     ) / lit * 100
abweichunglinks = abs(lit -zweilinks ) / lit * 100

print(f'Die Abweichung von der einseitigen          {abweichungeins}')
print(f'Die Abweichung von der zweiseitigen rechts  {abweichungrechts}')
print(f'Die Abweichung von der einseitigen links    {abweichunglinks}')