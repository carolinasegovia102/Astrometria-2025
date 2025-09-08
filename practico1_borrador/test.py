#%%
texto = "Hello" #En la terminal interactiva utilizamos uper para poner todo en mayuscula, antes definimos texto = "Hello rworld"
print(texto)

valor = 1. #En la terminal definimos texto = 1.0 y me da en type cuando pongo texto? me da type= float, inter o complex etc

entero = 3

complejo = 1j + 1
#%%

nombre = "Mario"
apellido = "Sgro"

print(nombre + apellido)
# %%

a = 1
b = 2

c = a + b
# %%

a = 1e4


# %%

a = 4**0.5 #raiz cuadrada
a = 4**(1/b)
# %%

#Si quieren calcular modulo (muy importante)

a = 13 % 10

#%%

def mifunc(): #El : me dice que ahi termina la definicion
    texto = "Hello world" #Bloque metido dentro de la definicion de def
    print(texto) #rdtructura de python

# %%

def mifunc(nombre): 
    texto = f"Hello, {nombre}!" #define un objeto de tipo stream
    print(texto)

#%%

def mifunc(nombre): 
    texto = f"Hello, {nombre}!"
    return texto #me permite redefinir a mifunc(1) = resultado, luego llamo a resultado

#%%

def mifunc(nombre, apellido): 
    texto = f"Hello, {nombre} {apellido}!" 
    return texto

def suma(a, b):
    c = a + b
    return c

# %%

def suma(a, b, d = 0):
    c = a + b + d
    return c

# %%

def suma(a, b, d = 0):
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
    c = a + b + d
    return c

# %%

import mis_funciones as misfuncs


# %%
print(misfuncs.suma(1,2))
# %%
