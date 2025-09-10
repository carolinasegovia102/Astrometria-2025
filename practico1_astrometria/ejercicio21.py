import numpy as np
from time import sleep #Para que el programa espere un poco antes de volver a preguntar


def monty_hall():

    vector = ['cabra', 'cabra', 'auto']
    while(True):
        puertas = np.random.permutation(vector)
        eleccion = int(input("Elija una puerta 1, 2 o 3:"))
        if puertas[eleccion-1] == "auto":
            print("gano")
        else:
            print("perdio")
        sleep(2)
#monty_hall()

def simular_monty_hall(n_simulaciones=10000):
    gana_cambiando = 0
    gana_sin_cambiar = 0

    for _ in range(n_simulaciones):
        puertas = ['cabra', 'cabra', 'auto']
        np.random.shuffle(puertas)
        eleccion = np.random.randint(0, 3)

        # El presentador abre una puerta con cabra que no fue elegida
        opciones_restantes = [i for i in range(3) if i != eleccion and puertas[i] == 'cabra']
        puerta_abierta = np.random.choice(opciones_restantes)

        # Si cambia, elige la otra puerta que no eligió ni fue abierta
        puerta_cambio = [i for i in range(3) if i != eleccion and i != puerta_abierta][0]

        # Estrategia: cambiar
        if puertas[puerta_cambio] == 'auto':
            gana_cambiando += 1

        # Estrategia: no cambiar
        if puertas[eleccion] == 'auto':
            gana_sin_cambiar += 1

    prob_cambiar = gana_cambiando / n_simulaciones
    prob_no_cambiar = gana_sin_cambiar / n_simulaciones
    print(f"Probabilidad de ganar cambiando: {prob_cambiar:.3f}")
    print(f"Probabilidad de ganar sin cambiar: {prob_no_cambiar:.3f}")

simular_monty_hall()
