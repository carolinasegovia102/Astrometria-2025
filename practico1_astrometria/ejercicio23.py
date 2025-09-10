import numpy as np
## Inciso a
'Notemos que el espacio esta formado por todos los pares {(d_1,d_2)}'
'Donde d_1 y d_2 pueden tomar los valores 1,2,3,4,5 y 6'
'Por lo tanto el espacio tiene 6*6=36 elementos'
'La variable aleatoria X es la suma de los dos dados'
##Inciso b
'Los eventos son: La suma es 2,3,4,5,6,7,8,9,10,11 o 12'
'Para 2 solo hay un par (1,1) por lo tanto P(2)=1/36'
'Para 3 hay dos pares (1,2) y (2,1) por lo tanto P(3)=2/36'
'Para 4 hay tres pares (1,3),(2,2) y (3,1) por lo tanto P(4)=3/36' 
'Para 5 hay cuatro pares (1,4),(2,3),(3,2) y (4,1) por lo tanto P(5)=4/36'
'Para 6 hay cinco pares (1,5),(2,4),(3,3),(4,2) y (5,1) por lo tanto P(6)=5/36'
'Para 7 hay seis pares (1,6),(2,5),(3,4),(4,3),(5,2) y (6,1) por lo tanto P(7)=6/36'
'Para 8 hay cinco pares (2,6),(3,5),(4,4),(5,3) y (6,2) por lo tanto P(8)=5/36'
'Para 9 hay cuatro pares (3,6),(4,5),(5,4) y (6,3) por lo tanto P(9)=4/36'
'Para 10 hay tres pares (4,6),(5,5) y (6,4) por lo tanto P(10)=3/36'
'Para 11 hay dos pares (5,6) y (6,5) por lo tanto P(11)=2/36'
'Para 12 hay un par (6,6) por lo tanto P(12)=1/36'
'Notemos que la suma de todas las probabilidades es 36/36=1'
'La distribucion de probabilidad queda:'
'X:    2   3   4   5   6   7   8   9   10  11  12'
'P(X): 1/36 2/36 3/36 4/36 5/36 6/36 5/36 4/36 3/36 2/36 1/36'
##Inciso c

import matplotlib.pyplot as plt

# Valores posibles de la suma y sus probabilidades teóricas
valores = np.arange(2, 13)
probs = np.array([1,2,3,4,5,6,5,4,3,2,1]) / 36

# Generar muestras según la distribución teórica
n_muestras = 10000
muestras = np.random.choice(valores, size=n_muestras, p=probs)

# Graficar la distribución empírica y la teórica
plt.figure(figsize=(8,4))
plt.hist(muestras, bins=np.arange(1.5,13.5,1), density=True, alpha=0.6, label='Empírica (simulada)')
plt.stem(valores, probs, linefmt='C1-', markerfmt='C1o', basefmt=" ", label='Teórica')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.title('Distribución de la suma de dos dados (teórica vs simulada)')
plt.legend()
plt.grid(True, axis='y', linestyle=':')
plt.show()

##Inciso d

# Simulación de lanzar dos dados n_muestras veces
dado1 = np.random.randint(1, 7, size=n_muestras)
dado2 = np.random.randint(1, 7, size=n_muestras)
suma_dados = dado1 + dado2

# Graficar la distribución empírica y la teórica
plt.figure(figsize=(8,4))
plt.hist(suma_dados, bins=np.arange(1.5,13.5,1), density=True, alpha=0.6, label='Empírica (simulada)')
plt.stem(valores, probs, linefmt='C1-', markerfmt='C1o', basefmt=" ", label='Teórica')
plt.xlabel('Suma de los dados')
plt.ylabel('Probabilidad')
plt.title('Distribución de la suma de dos dados (simulación vs teórica)')
plt.legend()
plt.grid(True, axis='y', linestyle=':')
plt.show()
