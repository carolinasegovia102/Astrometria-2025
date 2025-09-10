# %%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from funciones import generador_fibonacci
from funciones import coeficiente_correlacion_pearson
# %%
valores_fibonacci = generador_fibonacci(1000,10)
valores_numpy = np.random.rand(1000)

# Cálculo de correlación sin retardo
r_directo = coeficiente_correlacion_pearson(valores_fibonacci, valores_numpy)
print(f"Correlación directa Fibo vs NumPy: {r_directo:.6f}")

# Correlación con retardos
retardos = [1, 2, 3, 5, 7, 10]
resultados = []
for ret in retardos:
    r_fibo = coeficiente_correlacion_pearson(valores_fibonacci[:-ret], valores_fibonacci[ret:])
    r_numpy = coeficiente_correlacion_pearson(valores_numpy[:-ret], valores_numpy[ret:])
    resultados.append({"Retardo": ret,
                       "Fibo autocorrelación": r_fibo,
                       "NumPy autocorrelación": r_numpy})

df_corr = pd.DataFrame(resultados)
print("\nCorrelaciones con retardos:")
print(df_corr)



# %%
