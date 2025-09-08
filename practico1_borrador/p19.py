#%%
import matplotlib.pyplot as plt
from mis_funciones import generador_fibonacci   ##Recordar que si ya importe una vez la funcion, esto tiene memoria, entonces si lo modifico aveces hay que reiniciar el kernel (restart) porq piensa : ya lo importe, no hace falta importar de nuevo!! POR MAS QUE HAYA MODIFICADO LA FUNCIOOON.
import numpy as np

def ej19f1():
    x = generador_fibonacci(1000,142)
    _x = x[1:]
    _y = x[:-1]
    plt.plot(_x,_y,'ro')


# %%
ej19f1()
# %%

x = np.random.random(10)  ##genera numeros siguiendo una distribucion conocida. Puedo usarlo para el ejercicio de dados.
print(x)
# %%
