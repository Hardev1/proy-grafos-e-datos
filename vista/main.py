from controlador.Grafo import *
from recursos import *
import time
import json

with open('../recursos/caminos.json') as caminos:  # importa los caminos o aristas
    with open('../recursos/planetas.json') as planetas:  # importa los planetas o vertices
        galaxia = Grafo()
        listaPlanetas = json.load(planetas)
        caminos = json.load(caminos)

        # creacion de las cuevas desde el json
        for planeta in listaPlanetas['planetas']:
            galaxia.ingresarvertice(planeta['nombre'])

        print("¡Se cargaron los planetas exitosamente!")

print(galaxia.obtenerPlanetas()[1].getDato())