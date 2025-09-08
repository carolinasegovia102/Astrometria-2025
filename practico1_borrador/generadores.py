#%%

from mis_funciones import glc

numeros = glc(257,10) #Me genera 100 numeros con semilla x0=10
print(numeros)
# %%

## ¿Que valor de a y c escogemos, es arbitraria? = No!!!
## Generador lineal congruencia - Wikipedia : Lista de buenos valores para a y c, para probarlos. Valores que dan mas aletoriedad. Se hace un test de esos valores.
## Teorema que te dice que a y c tienen que ser coprimos u otra cosa para generar mas altoriedad.
## m = 2³²

## ¿De esos 257 numeros, cual se repite? Si algun numero se repite, se repite la secuencia.. ¿Como encuentro dicho numero?

# %%

semilla = 10
numeros = glc(257,semilla)

for i,n in enumerate(numeros) :
        if n == semilla:   ## Recordar que python cuenta desde 0. Basicamente el i me devuelve la celda en donde la semilla se repite. 
            print(i+1)     ##osea nunca se repite la semilla
# %%

semilla = 10
numeros = glc(257,semilla, a=37, c=1, M=156) ##Numeros entre 0 y 155, lo q me da en la terminal son las veces que se repiten y comienza la secuencia de nuevo, en i=12, en i=24 etc. Por numero de a y c no tengo ni siquiera 155 aleatorios, solo 12, 24 etc, q no se repiten.

for i,n in enumerate(numeros) :
        if n == semilla:  
            print(i+1) 
            break  #para la iteracion cuando se repite la semilla

# %%

##¿Como generamos funciones? - Ir a matplotlib, examples si no sabemos como hacer un grafico.

#%%
import matplotlib.pyplot as plt

# %%
## numeros[0:3] me devuelve en la terminal interactica los 3 primeros elementos.
## numeros[-1] me devuelve el ultimo numero

x = numeros[:-1] #defino variable x y me guardo todos los numeros excepto el ultimo
y = numeros [1:] #me guardo todos los numeros excepto el primero
plt.plot(x,y,'ro', label="pares") # label me define el titulo de la leyenda
plt.xlabel(r"$n_{i}$") #titulo ejes
plt.ylabel(r"$n_{i+1}$") #titulo ejes
plt.title("Titulo")
plt.legend()

## Un buen generador me devolveria puntitos aleatorios, el graafico que vemos claramente tiene cierta correladcion entre parametros.
# %%

## Me devuelve un buen generador, mirar el grafico.

semilla = 10
numeros = glc(1000,semilla, a=1664525,c=1013904223,M=2**32)

for i,n in enumerate(numeros):
        if n == semilla:   
            print(i+1) 
            break

x = numeros[:-1] #defino variable x y me guardo todos los numeros excepto el ultimo
y = numeros [1:] #me guardo todos los numeros excepto el primero
plt.plot(x,y,'ro', label="pares") # label me define el titulo de la leyenda
plt.xlabel(r"$n_{i}$") #titulo ejes
plt.ylabel(r"$n_{i+1}$") #titulo ejes
plt.title("Titulo")
plt.legend()semilla = 10
numeros = glc(1000,semilla, a=1664525,c=1013904223,M=2**32)

for i,n in enumerate(numeros):
        if n == semilla:   
            print(i+1) 
            break

x = numeros[:-1] #defino variable x y me guardo todos los numeros excepto el ultimo
y = numeros [1:] #me guardo todos los numeros excepto el primero
plt.plot(x,y,'ro', label="pares") # label me define el titulo de la leyenda
plt.xlabel(r"$n_{i}$") #titulo ejes
plt.ylabel(r"$n_{i+1}$") #titulo ejes
plt.title("Titulo")
plt.legend()
# %%

##¿Como generar un histograma?

# %%

plt.hist(numeros,bins="auto")
# %%
 ## En general, queremos numeros aleatorios entre 0 y 1, numeros tipos flotantes.
 ## Teniendo ese generador entre 0 y 1, uno quiere a partir de ese generar otra distribucion.
 ## Lo que se hace es dividir los numeros generados por M.

 # %%
## Voy a funciones a modificar &&&&&&&&&&&&&&&&&&&&
## Quiero normalizar el generador.

 # %%

from mis_funciones import glc
import matplotlib.pyplot as plt

semilla = 10
numeros = glc(1000,semilla, a=1664525,c=1013904223,M=2**32)

for i,n in enumerate(numeros):
        if n == semilla: #semilla es entero, n no lo es y por lo tanto python redondea como quiere, entonces a lo mejor no me detecta los numeros que se repiten, pues redondea como quiere.   
            print(i+1) 
            break

x = numeros[:-1] #defino variable x y me guardo todos los numeros excepto el ultimo
y = numeros [1:] #me guardo todos los numeros excepto el primero
plt.plot(x,y,'ro', label="pares") # label me define el titulo de la leyenda
plt.xlabel(r"$n_{i}$") #titulo ejes
plt.ylabel(r"$n_{i+1}$") #titulo ejes
plt.title("Titulo")
plt.legend()

# %%

plt.hist(numeros,bins="auto")

# %%

## Tengo que tener en cuenta que los numeros n que me devuelvan no sean iguales en el orden del beat de doble precision, si los numeros decimales en el orden de la precision son iguales me los toma como igual y entonces no estaria viendo exactamente donde se repite el numero, y ese seria el problema.
