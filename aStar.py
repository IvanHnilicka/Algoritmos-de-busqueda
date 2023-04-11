def aStar(nodo_inicial, grafo, heuristicas, nodo_objetivo):
    nodo_actual = nodo_inicial
    nodo_menor_costo = nodo_actual
    open.append(nodo_actual)


#   El algoritmo continua hasta llegar al nodo objetivo
    while nodo_actual != nodo_objetivo:      

        print("Open: ", open)
        print("Closed: ", closed)
        print("Nodo actual: ", nodo_actual)

#       Buscamos el nodo con menor euristica en la lista open
        for nodo in open:
            if grafo[nodo_actual].get(nodo):
#                print("Suma: ", heuristicas[nodo], "+", grafo[nodo_actual].get(nodo), " = ", heuristicas[nodo] + grafo[nodo_actual].get(nodo))
                if (heuristicas[nodo] + grafo[nodo_actual].get(nodo)) < (heuristicas[nodo_actual] + grafo[nodo_actual].get(nodo)):
                    nodo_menor_costo = nodo
        
        nodo_actual = nodo_menor_costo


#       Agregamos los adyacentes del nuevo nodo visitado
        for adyacente in grafo[nodo_actual]:
            open.append(adyacente)
        
        open.pop(open.index(nodo_actual))
        closed.append(nodo_actual)
        print("\n")

    print("\nRuta encontrada: ", closed)




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
    'Arad': { 'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140 },
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

"""""
grafo2 = {
    'Arad': { 'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140 },
    'Zerind': { 'Oradea': 71 },
    'Oradea': { 'Sibiu': 151 },
    'Timisoara': { 'Lugoj': 111 },
    'Lugoj': { 'Mehadia': 70 },
    'Mehadia': { 'Drobeta': 75 },
    'Drobeta': { 'Craiova': 120 },
    'Sibiu': { 'Fagaras': 99, 'Rimnicu Vilcea': 80 },
    'Craiova': { 'Rimnicu Vilcea': 146, 'Pitesti': 138 },
    'Rimnicu Vilcea': { 'Pitesti', 97 },
    'Pitesti': { 'Bucharest': 101 },
    'Fagaras': { 'Bucharest': 211 },
    'Bucharest': { 'Giurgiu': 90 },
    'Giurgiu': { },
    'Urziceni': { 'Vaslui': 142 , 'Hirsova': 98 },
    'Hirsova': { 'Eforie': 86 },
    'Eforie': { },
    'Vaslui': { 'Iasi': 92 },
    'Iasi': { 'Neamt': 87 },
    'Neamt': { }
}
"""


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

aStar('Arad', grafo2, heuristica2, 'Bucharest')