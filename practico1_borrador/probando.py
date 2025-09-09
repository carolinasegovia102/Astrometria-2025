
import numpy as np
Vacio = np.array([0,0,0])  ## Esto es un array vacio, no tiene elementos
Vacio.append(5)  ## Esto no funciona porque los arrays de numpy tienen tamaño fijo, no se pueden agrandar.
print(Vacio)