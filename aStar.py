def aStar(nodo_inicial, grafo, heuristicas, nodo_objetivo):
    costo_acumulado = 0
    nodo_actual = nodo_inicial
    pila.append(nodo_actual)

#   Agregamos el nodo inicial a la lista closed
    closed.append(nodo_inicial)

#   Agregamos sus nodos adyacentes a la lista open
    for adyacente in grafo[nodo_inicial]:
        open.append(adyacente)


#   El algoritmo sigue mientras no se haya llegado al nodo objetivo 
    while nodo_actual != nodo_objetivo:
        print("Open: ", open)
        print("Closed: ", closed)
        print("Pila: ", pila, "\n")

        costo_minimo = 999999999
        for nodo in open:
#           Comparamos costos si el nodo es adyacente al ultimo en la ruta
            if grafo[pila[-1]].get(nodo):
                if (grafo[pila[-1]][nodo] + heuristicas[nodo] + costo_acumulado) < costo_minimo:
                    costo_minimo = grafo[pila[-1]][nodo] + heuristicas[nodo]
                    nodo_actual = nodo
                    
#           Si no es adyacente quitamos el ultimo nodo de la ruta hasta encontrar uno que sea adyacente y comparamos
            else:
                while not grafo[pila[-1]].get(nodo):
                    pila.pop(-1)

#                   Si la ruta queda vacia generamos una nueva a partir del nodo que se esta comparando
                    if not pila:
                        nodo_ruta = nodo
                        for i in range(len(closed) - 1, -1, -1):
#                           Si los nodos son adyacentes lo agregamos a la ruta
                            if grafo[nodo_ruta].get(closed[i]) and grafo[closed[i]].get(nodo_ruta):
                                nodo_ruta = closed[i]
                                pila.insert(0, closed[i])
                        break

#               Comparamos el costo del nuevo nodo
                if (grafo[pila[-1]][nodo] + heuristicas[nodo] + costo_acumulado) < costo_minimo:
                    costo_minimo = grafo[pila[-1]][nodo] + heuristicas[nodo]
                    nodo_actual = nodo


#       Quitamos el nodo actual de la lista open y añadimos sus nodos adyacentes
        open.pop(open.index(nodo_actual))
        for adyacente in grafo[nodo_actual]:
            open.append(adyacente)


#       Si el nodo actual no es adyacente al ultimo de la ruta lo eliminamos
        while not grafo[pila[-1]].get(nodo_actual):
            pila.pop(-1)

#           Si la pila se queda vacía la llenamos con la nueva ruta
            if not pila:
                nodo = nodo_actual
                for i in range(len(closed) - 1, -1, -1):
#                   Si el nodo que se esta checando es adyacente lo agregamos al principio de la pila                    
                    if grafo[closed[i]].get(nodo):
                        nodo = closed[i]
                        pila.insert(0, nodo)
                break

#       Agregamos el nodo actual a la lista closed debido a que ya se visitó
        closed.append(nodo_actual)
        pila.append(nodo_actual)


    print("Ruta encontrada: ", pila)


#   Grafos debens ser no dirigidos
#   Nodo: [[adyacente, costo]]
grafo1 = {
    1: {
        2: 3, 
        3: 2
    }, 

    2: {
        1: 3,
        4: 4, 
        5: 1
    },

    3: {
        1: 2,
        6: 3,
        7: 1
    },

    4: {
        2: 4
    },

    5: {
        2: 1
    },

    6: {
        3: 3,
        8: 5
    },
    
    7: {
        3: 1,
        9: 2,
        10: 3
    },

    8: {
        6: 5
    },
    9: {
        7: 2
    },
    10: {
        7: 3
    }
}


#   Nodo: heuristica
heuristica1 = {
    1: 13,
    2: 12,
    3: 4,
    4: 7,
    5: 3,
    6: 8,
    7: 2,
    8: 4,
    9: 9,
    10: 0
}


#   Nodo: { Adyacente: costo }
grafo2 = {
    'Arad': { 'Sibiu': 140, 'Timisoara': 118, 'Zerind': 75 },
    'Zerind': { 'Oradea': 71, 'Arad': 75 },
    'Oradea': { 'Sibiu': 151, 'Zerind': 71 },
    'Timisoara': { 'Lugoj': 111, 'Arad': 118 },
    'Lugoj': { 'Mehadia': 70, 'Timisoara': 111 },
    'Mehadia': { 'Drobeta': 75, 'Lugoj': 70 },
    'Drobeta': { 'Craiova': 120, 'Mehadia': 75 },
    'Sibiu': { 'Fagaras': 99, 'Rimnicu Vilcea': 80, 'Oradea': 151, 'Arad': 140 },
    'Craiova': { 'Rimnicu Vilcea': 146, 'Pitesti': 138, 'Drobeta': 120 },
    'Rimnicu Vilcea': { 'Pitesti': 97, 'Craiova': 146, 'Sibiu': 80 },
    'Pitesti': { 'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97 },
    'Fagaras': { 'Bucharest': 211, 'Sibiu': 99 },
    'Bucharest': { 'Giurgiu': 90, 'Pitesti': 101, 'Urziceni': 85, 'Fagaras': 211 },
    'Giurgiu': { 'Bucharest': 90 },
    'Urziceni': { 'Vaslui': 142 , 'Hirsova': 98, 'Bucharest': 85 },
    'Hirsova': { 'Eforie': 86, 'Urziceni': 98 },
    'Eforie': { 'Hirsova': 86 },
    'Vaslui': { 'Iasi': 92, 'Urziceni': 142 },
    'Iasi': { 'Neamt': 87, 'Vaslui': 92 },
    'Neamt': { 'Iasi': 87 }
}


#   Nodo: Heuristica
heuristica2 = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}



open = []
closed = []
pila = []

aStar(1, grafo1, heuristica1, 10)