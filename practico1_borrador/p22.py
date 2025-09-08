# %%
import matplotlib.pyplot as plt
from mis_funciones import generador_galaxias
import numpy as np

def ej22():
    g = generador_galaxias(10000) 
    print(np.unique(g, return_counts=True))

g = generador_galaxias(10000)
print(g)

x, y = np.unique(g,return_counts=True)
print(x)
print(y)

plt
#%%

ej22()


# %%
def ejemplo():
    nombre = input ("ingrese su nombre: ")
    edad = int(input("ingrese su edad"))
    anio_de_nacimiento = 2025 - edad
    print(f"Su nombre es {nombre}")  # "f" quiero imprimir la variable nombre, reeal¿mplaza todo lo que esta dentro de llaves por el valor de la variable
    print(f"su año de nacimiento fue: {anio_de_nacimiento}") #tambien se le puede agregar formato
ejemplo()
# %%
