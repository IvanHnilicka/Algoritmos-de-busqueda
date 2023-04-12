def lbs(nodo_inicial, nodo_objetivo, grafo, heuristicas, beam):
    nodos = []
    frontera.append(nodo_inicial)

    print("Frontera: ", frontera)        
    print("Explorados: ", explorados, "\n")

    frontera.clear()
    explorados.append(nodo_inicial)

    for adyacente in grafo[nodo_inicial]:
        nodos.append(adyacente)

    while not explorados.count(nodo_objetivo):
        contador = len(nodos)

        if contador == beam:
            for nodo in nodos:
                frontera.append(nodo)
            nodos.clear()
        else:
            while contador > beam:
                nodo_mayor_costo = nodos[0]

                for nodo in nodos:
                    if heuristicas[nodo] > heuristicas[nodo_mayor_costo]:
                        nodo_mayor_costo = nodo

                nodos.pop(nodos.index(nodo_mayor_costo))
                contador -= 1

            for nodo in nodos:
                frontera.append(nodo)
            nodos.clear()


        print("Frontera: ", frontera)        
        print("Explorados: ", explorados, "\n")


        for nodo in frontera:
            explorados.append(nodo)

            for adyacente in grafo[nodo]:
                nodos.append(adyacente)

        frontera.clear()

    print("Frontera: ", frontera)
    print("Explorados: ", explorados)



#   Nodo: [ adyacentes ]
grafo1 = {
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
    'S': 10,
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



grafo2 = {
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

lbs('A', 'J', grafo2, heuristica2, 3)