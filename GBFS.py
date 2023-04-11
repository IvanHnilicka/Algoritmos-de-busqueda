def gbfs(nodo_inicial, grafo, heuristicas, nodo_objetivo):
    nodo_actual = nodo_inicial
    open.append(nodo_actual)

#   Ingresa los nodos adyacentes del nodo inicial a la lista open
    for adyacente in grafo[nodo_inicial]:
        open.append(adyacente[0])



#   El algoritmo continua hasta llegar al nodo objetivo
    while nodo_actual != nodo_objetivo:
        closed.append(nodo_actual)
        open.pop(open.index(nodo_actual))

        for nodo in open:
            if heuristicas[nodo] < heuristicas[nodo_actual]:
                nodo_actual = nodo

        for adyacente in grafo[nodo_actual]:
            open.append(adyacente[0])

    open.pop(open.index(nodo_actual))
    closed.append(nodo_actual)

    print("Ruta encontrada: ", closed)



grafo1 = {
#   Nodo: [[adyacente, costo]]
    1: [
        [2, 3], 
        [3, 2]
       ], 

    2: [
        [4, 4], 
        [5, 1]
       ],

    3: [
        [6, 3],
        [7, 1]
       ],

    4: [],

    5: [],

    6: [
        [8, 5]
       ],
    
    7: [
        [9, 2],
        [10, 3]
       ],

    8: [],
    9: [],
    10: []
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


grafo2 = {
    'Arad': [['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]],
    'Zerind': [['Oradea', 71]],
    'Oradea': [['Sibiu', 151]],
    'Timisoara': [['Lugoj', 111]],
    'Lugoj': [['Mehadia', 70]],
    'Mehadia': [['Dobreta', 75]],
    'Dobreta': [['Craiova', 120]],
    'Sibiu': [['Fagaras', 99], ['Rimnicu Vilcea', 80]],
    'Craiova': [['Rimnicu Vilcea', 146], ['Pitesti', 138]],
    'Rimnicu Vilcea': [['Pitesti', 97]],
    'Pitesti': [['Bucharest', 101]],
    'Fagaras': [['Bucharest', 211]],
    'Bucharest': [['Giurgiu', 90]],
    'Giurgiu': [],
    'Urziceni': [['Vaslui', 142], ['Hirsova', 98]],
    'Hirsova': [['Eforie', 86]],
    'Eforie': [],
    'Vaslui': [['Iasi', 92]],
    'Iasi': [['Neamt', 87]],
    'Neamt': []
}


heuristica2 = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}



open = []
closed = []

gbfs('Arad', grafo2, heuristica2, 'Bucharest')