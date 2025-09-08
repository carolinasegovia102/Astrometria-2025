#%%
import numpy as np
def suma(a, b, d = 5, e = 6):
    """
    Esta funcion hace la suma de a con b, y opcionalmente

    Parametros:
        a:
        b:
        d (opcional):
    Devuelve:
        c
    Modo de uso:
        c = suma (1,2,d=4)
    """
    c = a + b + d + e
    return c
# %%

##def glc(a,c,M,x0): # = numero pseudo aleatorio (caso determinista) - Tengo un algoritmo de creacion, puedo predecir el siguiente. Queremos tener cierto control justamente ccomo son generados los numeros.
   ## x = (c + a*x0) % M #Esto es una operacion, a y c parametros del generador, x0 semilla generadora, resultado entero y maximo (m-1)
    ##return x                  # x es el generador, M=32 y yo genero 32 o mas dependiendo de los valores de a y b.

#¿Como genero numeros aleatorios? = variando el x0 (incomodo hacerlo a mano) - incomodo!!! hacemos lo siguiente
# %%

def glc(n, x0, a=57, c=1, M=256): #n es el numero de cuantos numeros aleatorio quiero generar
    numeros = [] # Una lista ṕuede contener valores de diferentes tipos, para menos complicaciones lo pensamos como un vector
    for i in range(n): # El n toma valores entre 0 y n-1. Hace una integracion me repite la cuenta del x pero n veces (x nro pseudo aleatorio)
        x = (c + a*x0) % M
        numeros.append(x) # Primero lista vacia, luego le doy de comer un x0, genera un x, ese x ahora lo defino coo el nuevo x0, y eso lo hace n veces. 
        x0 = x
    return numeros #Recordar que poniendo otro valor especifico de M creo un nuevo generador.
# %%

## Modificamos &&&&&&&&&&&&&&&&&&

def glc(n, x0, a=57, c=1, M=256): 
    numeros = [] 
    for i in range(n): 
        x = (c + a*x0) % M
        numeros.append(x/M)
        x0 = x
    return numeros 

# %%
def generador_congruencia_lineal_enteros(n, x0, a=1664525, c=1013904223, M=2**32):
    numeros = []
    for i in range (n):
            x = (c + a*x0) % M   ##me devuelve lista de numeros de enteros
            numeros.append(x)    ## no puedo hacer division entre lista y entero pero si tipo np.array y enteros
            x0 = x
    return numeros

## normalizado
def generador_congruencia_lineal(n, x0, a=664525, c=1013904223, M=2**32):
    return np.array(generador_congruencia_lineal_enteros(n,x0,a,c,M))/M #Objeto de python que tiene valores y metodos asociados (np.array a diferencia de listas solo admiten valores del mismo tipo todos flotanntes por ejemplo)



# %%
######## GENERADOR DE FIBONACCI CON RETARDO#########

def generador_fibonacci_enteros(n, x0, j=24, k=55, m=2**32):
    numeros = generador_congruencia_lineal_enteros(k, x0) #Con esto genero de 0 hasta (k-1). Me devuelve lista con k-1 elementos.
    for i in range(k, k + n): #Esto va de k hasta k+(n-1) pues python comienza a contar desde cero.
        numeros.append((numeros[i-j] + numeros[i-k]) % m)  #Resultado pseudoaletorio, este numero estara entre 0 y (2**32 - 1)
    return numeros[k:] #Notar que pido los numeros de k en adelante, es decir quiero n y por lo tanto me deshago de los k de congruencia lineal.

def generador_fibonacci(n, x0, j=24, k=55, m=2**32):
    return np.array(generador_fibonacci_enteros(n,x0,j,k,m))/m
# %%

####EJERCICIO 22#######

def generador_galaxias(n):
    galaxias = []

    X = generador_fibonacci(n,142)
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


f"{np.pi:4.2f}" #me deja 2 decimales despues de la coma, lo corro en el interactivo.
f"{np.pi:5.3f}" #me deja 3

# %%
#=============== EJ21==========
def monty_hall():

    vector = ['cabra', 'cabra', 'auto']
    while(True):
        puertas = np.random.permutation(vector)
        eleccion = int(input("Elija una puerta 1, 2 o 3:"))
        if puertas[eleccion-1] == "auto":
            print("gano")
        else:
            print("perdio")
        sleep(0.1)
# %%
