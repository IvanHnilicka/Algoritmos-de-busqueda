def aStar(nodo_inicial, grafo, heuristicas, nodo_objetivo):
    nodo_actual = [nodo_inicial, 0]
    pila.append(nodo_actual)
    closed.append(nodo_actual)

#   Almacena los posibles caminos desde el nodo inicial en open
    for adyacente in grafo[nodo_inicial]:
        open.append(adyacente)    


#   Seguimos explorando mientras haya caminos disponibles en open
    while open:
#       Busca el camino de menor costo
        costo_minimo = 999999999
        for i in range(0, len(open)):
            if open[i][1] + heuristicas[open[i][0]] <= costo_minimo:
                costo_minimo = open[i][1] + heuristicas[open[i][0]]
                nodo_actual = open[i]
            
#       Removemos el nodo con menor costo de open debido a que ya se visitó
        open.pop(open.index(nodo_actual))
            
#       Agregamos a open los caminos adyacentes del nodo visitado
        for adyacente in grafo[nodo_actual[0]]:
#           Si el nodo ya fue visitado previamente lo omitimos
            if closed.count(adyacente):
                continue
            open.append(adyacente)
        
#       Si el actual no es adyacente al ultimo de la ruta lo quitamos de la ruta
        while not grafo[pila[-1][0]].count(nodo_actual):
            pila.pop(-1)

#           Si la pila se queda vacía generamos el camino hasta llegar al nodo actual
            if not pila:
                nodo = nodo_actual
#               Checamos los nodos closed para generar el camino hacia atrás a partir de ellos                          
                for i in range(len(closed) - 1, -1, -1):
#                   Si el nodo que se esta checando es adyacente lo agregamos al principio de la pila                    
                    if grafo[closed[i][0]].count(nodo):
                        nodo = closed[i]
                        pila.insert(0, nodo)
                break


        pila.append(nodo_actual)
        closed.append(nodo_actual)

#       Si el nodo actual es el nodo objetivo calculamos el costo de la ruta actual
        if(nodo_actual[0] == nodo_objetivo):
            costo_actual = 0
            print("Ruta: ", end = "")
#           Validaciones para dar formato de impresión en consola
            for i in range(0, len(pila)):
                costo_actual += pila[i][1]
                if i != len(pila) - 1:
                    print(pila[i][0], end = " - ")
                else:
                    print(pila[i][0])

            print("Costo de ruta: ", costo_actual)
            return



grafo1 = {
    1: [[2, 3], [3, 2]],
    2: [[4, 4], [5, 1]],
    3: [[6, 3], [7, 1]],
    4: [[2, 4]],
    5: [[2, 1]],
    6: [[8, 5]] ,
    7: [[9, 2], [10, 3]],
    8: [[6, 5]],
    9: [[7, 2]],
    10: [[7, 3]]
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
    'Eforie': [['Hirsova', 86]],
    'Vaslui': [['Iasi', 92], ['Urziceni', 142]],
    'Iasi': [['Neamt', 87], ['Vaslui', 92]],
    'Neamt': [['Iasi', 87]]
}



#   Nodo: Heuristica
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
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


grafo3 = {
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
pila = []

# aStar(1, grafo1, heuristica1, 10)
aStar('S', grafo3, heuristica3, 'G')