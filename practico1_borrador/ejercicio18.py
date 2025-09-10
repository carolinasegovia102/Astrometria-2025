# %%

import numpy as np
import matplotlib.pyplot as plt
from funciones import generador_congruencia_lineal_enteros
from funciones import generador_congruencia_lineal

# %%
#==================================EJERCICIO 18=========================================

################INCISO (a): programa para detecar periodo en gcl - normalizado


def generador_congruencia_lineal_enteros(n, x0, a=57, c=1, M=256): #definicion de la funcion
    numeros = [] #lista vacia donde se guardara la secuencia generada
    for i in range(n): #bucle que genera n numeros (se repite n veces). Notar que i se mueve entre 0 y n-1
        i = i + 1 #hago que i se mueva entre 0 y n
        x = (c + a*x0) %M #formula del GCL
        if x == 10: #forma de edetectar el periodo
            print(i,x) #si el valor generado es igual a la semilla inicial x0, imprime el paso y el valor
        numeros.append(x) #tranforma la secuencia de enteros en una de nros reales y se divide por M porque es el valor maximo posible del rango de enteros generados
        x0 = x #garantiza que tome como primer valor el x0, actualiza el valor para la proxima iteracion
    print(numeros)
    return(numeros) #devuelve lista completa de numeros generados
#Trabajar con numpy(array) es mas preciso que hacerlo con listas(append).
def generador_congruencia_lineal(n, x0, a=57, c=1, M=256):
    return np.array(generador_congruencia_lineal_enteros(n,x0,a,c,M))/M
numeros = generador_congruencia_lineal(1000, 10)

#%%

#################INCISO (a): programa para plotear la secuencia y poder ver si existen patrones en gcl


# Graficar pares consecutivos (Ni, Ni+1)
plt.figure(figsize=(6,6))
plt.scatter(numeros[:-1], numeros[1:], s=10, alpha=0.7)
plt.xlabel(r"$N_i$")
plt.ylabel(r"$N_{i+1}$")
plt.title("Correlación entre pares consecutivos generados con gcl")
plt.grid(True)
plt.show()


#%%

################INCISO (a): programa redefiniendo los parametros de la funcion generadora (alta calidad) y ploteo de la secuencia


def generador_alta_calidad_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    numeros_a = [] 
    for i in range(n): 
        i = i + 1 
        x_a = (c + a*x0) %M 
        if x_a == 10: 
            print(i,x_a) 
        numeros_a.append(x_a) 
        x0 = x_a 
    print(numeros_a)
    return(numeros_a) 
def generador_alta_calidad(n, x0, a=1664525, c=1013904223, M=2**32):
    return np.array(generador_alta_calidad_enteros(n,x0,a,c,M))/M

numeros_a = generador_alta_calidad(1000, 10)

plt.figure(figsize=(6,6))
plt.scatter(numeros_a[:-1], numeros_a[1:], s=10, alpha=0.7)
plt.xlabel(r"$N_i$")
plt.ylabel(r"$N_{i+1}$")
plt.title("Correlación entre pares consecutivos generador de alta calidad")
plt.grid(True)
plt.show()


#%%

###############INCISO (a): obtencion de momento de orden k=(1,3,7) teorico y empirico para la distribucion de numeros obtenida con (n=10,100,1000).


def generador_alta_calidad_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    numeros_a = [] 
    for i in range(n): 
        i = i + 1 
        x_a = (c + a*x0) %M 
        if x_a == 10: 
            print(i,x_a) 
        numeros_a.append(x_a) 
        x0 = x_a 
    print(numeros_a)
    return(numeros_a) 
def generador_alta_calidad(n, x0, a=1664525, c=1013904223, M=2**32):
    return np.array(generador_alta_calidad_enteros(n,x0,a,c,M))/M


def momentos(numeros_a, ks=(1,3,7)):
    empirico = {k: np.mean(numeros_a**k) for k in ks}
    teorico = {k: 1/(k+1) for k in ks}
    return empirico, teorico

for n in (10, 100, 1000): #inicia bucle que va a repetirse tres veces, tomando distintos valores de n en cada iteracion
    numeros_a = generador_alta_calidad(n, 10) #es un array de long. n con los nros generados, llamo a mi funcion para generar n numeros pseudoaleatorios normalizados en [0,1]
    empirico, teorico = momentos(numeros_a) #llamo a funcion momentos y le paso el array, aqui se calcula los momentos empiricos y teoricos
    print(f"\nn = {n}")
    for k in (1,3,7):
        error = empirico[k] - teorico[k]
        print(f"  M{k}: empírico = {empirico[k]:.6f} | teórico = {teorico[k]:.6f} | error = {error:+.6f}")


#%%

#################INCISO (b): 


N_caminatas = 10
N_pasos = 1000
x = np.zeros((N_caminatas, N_pasos)) ## Crea un array de numpy con todos ceros, tiene N_caminatas filas por N_pasos filas. Todos cero
y = np.zeros((N_caminatas, N_pasos))
#Lo siguiente genera una matriz X y una matriz Y de 10 filas y 1000 columnas, donde cada fila es una caminata diferente y cada columna es un paso diferente.
for i in range(N_caminatas):
    for j in range(1, N_pasos): ## El 1 se agrega para que el primer salto sea 1. Todo se inicia en el 0 luego el primer salto a 1.
        salto = np.random.rand()*2*np.sqrt(2) - np.sqrt(2)  ## Me tira numeros entre 0 y 1. Yo quiero entre -raiz de 2 y raiz de 2. Un escalado y una traslacion
        x[i,j] = x[i, j-1] + salto
        salto = np.random.rand()*2*np.sqrt(2) - np.sqrt(2)
        y[i,j] = y[i, j-1] + salto
        ## El salto en y es independiente del salto en x. Cada uno tiene su propio random.

for i in range(N_caminatas):
    plt.plot(x[i],y[i])


#Queremos calcular el valor de expectacion de cada paso, es decir el promedio de las distancias del paso 1 de todas las caminatas
distancia = np.sqrt(x**2 + y**2) ## Distancia al origen en cada paso de cada caminata. Es una matriz 10x1000
valor_de_expectacion = np.mean(distancia, axis=0) #Me devuelve un vector (lista) de 1000 elementos, el promedio de la distanacia de cada paso de todas las caminatas
pasos = np.arange(N_pasos) ## Vector de 0 a 999, los pasos


# Configuramos la figura para mostrar dos gráficos
plt.figure(figsize=(14, 6))

# Gráfico 1: Valor esperado de R en función del paso N
for i in range(N_caminatas):
    
    plt.subplot(1, 2, 1)
    plt.plot(pasos, distancia[i], alpha=0.3)  # Graficar cada caminata individualmente con transparencia
    plt.plot(pasos, valor_de_expectacion,color='k')
    plt.title('Valor Esperado de la Distancia vs. Número de Pasos (N)')
    plt.xlabel('Número de Paso (N)')
    plt.ylabel('Valor Esperado de R, E[R]')
    plt.grid(True)
    

    # Gráfico 2: Valor esperado de R en función de la raíz cuadrada del paso N
    plt.subplot(1, 2, 2)
    plt.plot(np.sqrt(pasos), valor_de_expectacion,color='k')
    plt.title(r'Valor Esperado de la Distancia vs. $\sqrt{N}$')
    plt.xlabel(r'$\sqrt{N}$')
    plt.ylabel('Valor Esperado de R, E[R]')
    plt.grid(True)
    

plt.tight_layout()
plt.show()

