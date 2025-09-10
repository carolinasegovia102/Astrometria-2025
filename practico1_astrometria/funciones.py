# %%
import numpy as np

# %%

#==================================EJERCICIO 18=========================================


############## inciso (a):


def generador_congruencia_lineal_enteros(n, x0, a=57, c=1, M=256): #definicion de la funcion
    numeros = [] #lista vacia donde se guardara la secuencia generada
    for i in range(n): #bucle que genera n numeros (se repite n veces). Notar que i se mueve entre 0 y n-1
        i = i + 1 #hago que i se mueva entre 1 y n
        x = (c + a*x0) %M #formula del GCL
        numeros.append(x) #guarda la lista
        x0 = x #garantiza que tome como primer valor el x0, actualiza el valor para la proxima iteracion
    return(numeros) #devuelve lista completa de numeros generados



#####ESTA FUNCION ES LA QUE ESTA NORMALIZADA ENTRE 0 Y 1########
def generador_congruencia_lineal(n, x0, a=57, c=1, M=256):
    return np.array(generador_congruencia_lineal_enteros(n,x0,a,c,M))/M
#Trabajar con numpy(array) es mas preciso que hacerlo con listas(append). Por esa razon convierto la lista en array y luego lo normalizo dividiendo por M.



def generador_alta_calidad_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    numeros_a = [] 
    for i in range(n): 
        i = i + 1 
        x_a = (c + a*x0) %M 
        numeros_a.append(x_a) 
        x0 = x_a 
    return(numeros_a) 



#####ESTA FUNCION ES LA QUE ESTA NORMALIZADA ENTRE 0 Y 1########
def generador_alta_calidad(n, x0, a=1664525, c=1013904223, M=2**32):
    return np.array(generador_alta_calidad_enteros(n,x0,a,c,M))/M
# numeros_a es un array de numpy con n numeros pseudoaleatorios normalizados en [0,1]



def momentos(numeros_a, ks=(1,3,7)):
    empirico = {k: np.mean(numeros_a**k) for k in ks}
    teorico = {k: 1/(k+1) for k in ks}
    return empirico, teorico




#################INCISO (b): 


# %%

#==================================EJERCICIO 19=========================================



def generador_fibonacci_enteros(n, x0, j=24, k=55, m=2**32):
    numeros = generador_congruencia_lineal_enteros(k, x0) #Con esto genero de 0 hasta (k-1). Me devuelve lista con k-1 elementos.
    for i in range(k, k + n): #Esto va de k hasta k+(n-1) pues python comienza a contar desde cero.
        numeros.append((numeros[i-j] + numeros[i-k]) % m)  #Resultado pseudoaletorio, este numero estara entre 0 y (2**32 - 1)
    return numeros[k:] #Notar que pido los numeros de k en adelante, es decir quiero n y por lo tanto me deshago de los k de congruencia lineal.

def generador_fibonacci(n, x0, j=24, k=55, m=2**32):
    return np.array(generador_fibonacci_enteros(n,x0,j,k,m))/m
#numeros es un array de numpy con n numeros pseudoaleatorios normalizados en [0,1] del generador de Fibonacci.




# %%
#==================================EJERCICIO 20=========================================

def coeficiente_correlacion_pearson(x, y):
    """
    Calcula el coeficiente de correlación de Pearson entre dos variables x e y.

    Parámetros:
    x (array-like): Primera variable. # x e y son arrays de igual longitud
    y (array-like): Segunda variable.

    Retorna (returns):
    float: Coeficiente de correlación de Pearson.
    r: Coefficiente de correlacion de Pearson
    """
    # Convierto x e y en arrays de numpy
    x = np.array(x)
    y = np.array(y)

    #Verificar que tienen la misma longitud
    n = len(x)
    if n != len(y):
        raise ValueError("Las listas x e y deben tener la misma longitud.")
    
    # Cálculo del coeficiente de correlación de Pearson
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
    
    # Evitar división por cero
    if denominator == 0:
        return 0  
    
    r = numerator / denominator
    return r
#%%

#==================================EJERCICIO 22=========================================


def generador_galaxias(n):
    galaxias = []

    X = generador_fibonacci(n,10)
    for x in X:
        if (0 <= x) and (x < 0.4):
            galaxias.append("eliptica")
        elif (0.4 <= x) and (x < 0.7):
            galaxias.append("espiral")
        elif (0.7 <= x) and (x < 0.9):
            galaxias.append("enana")
        else:
            galaxias.append("irregular")
    return galaxias




# %%
