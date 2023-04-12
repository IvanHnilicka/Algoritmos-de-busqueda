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
        nodo_actual = open[0]

#       Buscamos el nodo con menor euristica en la lista open
        for nodo in open:
            if heuristicas[nodo] < heuristicas[nodo_actual]:
                nodo_actual = nodo

#       Agregamos los adyacentes del nuevo nodo visitado
        for adyacente in grafo[nodo_actual]:
            if closed.count(adyacente):
                continue

            if open.count(adyacente):
                continue
            open.append(adyacente[0])


#   Quitamos el nodo visitado de la lista open y lo agregamos en la lista closed
    open.pop(open.index(nodo_actual))
    closed.append(nodo_actual)


    print("Ruta encontrada: ", end=" ")   
#   Validaciones para dar formato de impresión en consola
    for nodo in closed:
        if nodo != closed[-1]:
            print(nodo, end=" - ")
        else:
            print(nodo)



grafo_heuristica_1 = {
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



grafo_heuristica_2 = {
    'Arad': [['Zerind', 75], ['Timisoara', 118], ['Sibiu', 140]],
    'Zerind': [['Oradea', 71], ['Arad', 75]],
    'Oradea': [['Sibiu', 151], ['Zerind', 71]],
    'Timisoara': [['Lugoj', 111], ['Arad', 118]],
    'Lugoj': [['Mehadia', 70], ['Timisoara', 111]],
    'Mehadia': [['Dobreta', 75], ['Lugoj', 70]],
    'Dobreta': [['Craiova', 120], ['Mehadia', 75]],
    'Sibiu': [['Fagaras', 99], ['Rimnicu Vilcea', 80], ['Arad', 140], ['Oradea', 151]],
    'Craiova': [['Rimnicu Vilcea', 146], ['Pitesti', 138], ['Dobreta', 120]],
    'Rimnicu Vilcea': [['Pitesti', 97], ['Sibiu', 80]],
    'Pitesti': [['Bucharest', 101], ['Rimnicu Vilcea', 97], ['Craiova', 138]],
    'Fagaras': [['Bucharest', 211], ['Sibiu', 99]],
    'Bucharest': [['Giurgiu', 90], ['Pitesti', 101], ['Fagaras', 211], ['Urziceni', 85]],
    'Giurgiu': [['Bucharest', 90]],
    'Urziceni': [['Vaslui', 142], ['Hirsova', 98], ['Bucharest', 85]],
    'Hirsova': [['Eforie', 86], ['Urziceni', 98]],
    'Eforie': ['Hirsova', 86],
    'Vaslui': [['Iasi', 92], ['Urziceni', 142]],
    'Iasi': [['Neamt', 87], ['Vaslui', 92]],
    'Neamt': [['Iasi', 87]]
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


grafo_heuristica_3 = {
    'S': [['A', 5], ['B', 9], ['D', 6]],
    'A': [['B', 3], ['G', 9]],
    'B': [['A', 2], ['C', 1]],
    'C': [['S', 6], ['G', 5], ['F', 7]],
    'D': [['S', 1], ['C', 2], ['E', 2]],
    'E': [['G', 7]],
    'F': [['D', 2], ['G', 8]],
    'G': []

}

heuristica3 = {
    'S': 5,
    'A': 7,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 5,
    'F': 6,
    'G': 0
}



open = []
closed = []

gbfs(1, grafo_heuristica_1, heuristica1, 10)
# gbfs('Arad', grafo_heuristica_2, heuristica2, 'Bucharest')
# gbfs('S', grafo_heuristica_3, heuristica3, 'G')