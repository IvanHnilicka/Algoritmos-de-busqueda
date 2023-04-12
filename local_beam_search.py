def lbs(nodo_inicial, nodo_objetivo, grafo, heuristicas, beam):
#   Almacena todos los posibles caminos que se pueden visitar
    nodos = []
    frontera.append(nodo_inicial)

    print("Frontera: ", frontera)        
    print("Explorados: ", explorados, "\n")

    frontera.clear()
    explorados.append(nodo_inicial)

#   Agregamos los adyacentes del nodo inicial a la lista de posibles caminos
    for adyacente in grafo[nodo_inicial]:
        nodos.append(adyacente)

#   El algoritmo continua hasta haber explorado el nodo objetivo
    while not explorados.count(nodo_objetivo):
        contador = len(nodos)

#       Si tenemos el mismo numero de caminos disponibles que el limite los agregamos directamente
        if contador == beam:
            for nodo in nodos:
                frontera.append(nodo)
            nodos.clear()
#       Si no eliminamos aquellos de mayor costo hasta tener solo los que cumplan con el limite
        else:
            while contador > beam:
                nodo_mayor_costo = nodos[0]

#               Buscamos el nodo de mayor costo de entre todos los disponibles
                for nodo in nodos:
                    if heuristicas[nodo] > heuristicas[nodo_mayor_costo]:
                        nodo_mayor_costo = nodo

#               Lo eliminamos y reducimos el contador en 1 debido a que ya tenemos 1 camino dispoible menos
                nodos.pop(nodos.index(nodo_mayor_costo))
                contador -= 1

#           Agregamos los nodos que quedaron a la frontera
            for nodo in nodos:
                frontera.append(nodo)
            nodos.clear()


        print("Frontera: ", frontera)        
        print("Explorados: ", explorados, "\n")

#       Pasamos los nodos de la frontera a los explorados
        for nodo in frontera:
            explorados.append(nodo)
#           Agregamos los adyacentes de los nodos en la frontera debido a que ya se visitaron
            for adyacente in grafo[nodo]:
                nodos.append(adyacente)

#       Reiniciamos la frontera para tener solo los nuevos nodos de la siguiente iteracion
        frontera.clear()

    print("Frontera: ", frontera)
    print("Explorados: ", explorados)



#   Nodo: [ adyacentes ]
LocalBeamSearch1 = {
    'S': ['A', 'B'],
    'A': ['C','D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': [],
    'E': ['I', 'J'],
    'F': [],
    'G': [],
    'H': ['K', 'L'],
    'I': [],
    'J': ['M', 'N'],
    'K': [],
    'L': [],
    'M': [],
    'N': []
}

#   Nodo: heuristica
heuristica1 = {
    'S': 12,
    'A': 7,
    'B': 10,
    'C': 5,
    'D': 8,
    'E': 6,
    'F': 9,
    'G': 6,
    'H': 4,
    'I': 7,
    'J': 5,
    'K': 2,
    'L': 0,
    'M': 3,
    'N': 1
}



LocalBeamSearch2 = {
    'A': ['B', 'C', 'D'],
    'B': ['G', 'H'],
    'C': [],
    'D': ['E', 'F'],
    'E': ['L'],
    'F': ['M'],
    'G': ['I'],
    'H': ['J', 'K'],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}

heuristica2 = {
    'A': 18,
    'B': 12,
    'C': 15,
    'D': 16,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 13,
    'I': 3,
    'J': 0,
    'K': 1,
    'L': 3,
    'M': 2
}



frontera = []
explorados = []

lbs('S', 'L', LocalBeamSearch1, heuristica1, 2)
# lbs('A', 'J', LocalBeamSearch2, heuristica2, 3)