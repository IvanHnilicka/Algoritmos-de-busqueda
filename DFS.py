def dfs(nodo, visitados, grafo):

#   Marca como visitado el nodo actual
    visitados[nodo] = True
    print(nodo)

#   Checamos si hay nodos adyacentes que no han sido visitados
    for adyacente in grafo[nodo]:

#       Llamamos a la función con cada nodo adyacente que no haya sido visitado
        if not visitados[adyacente]:
            dfs(adyacente, visitados, grafo)



# Grafo1
grafo = {
#   Nodo: [adyacentes]
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [7, 8],
    6: [9],
    7: [],
    8: [],
    9: []
}

"""""
# Grafo2
grafo = {
    1: [],
    3: [1, 6],
    4: [],
    6: [4, 7],
    7: [],
    8: [3, 10],
    10: [14],
    13: [],
    14: [13]
}
"""


visitados = { nodo: False for nodo in grafo }

nodo_inicial = 1
dfs(nodo_inicial, visitados, grafo)