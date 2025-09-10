#%%
import numpy as np
from funciones import generador_fibonacci
from funciones import generador_galaxias

galaxia = generador_galaxias(10000)
print(np.unique(galaxia, return_counts=True))

# %%
