def bfs(nodo_inicial, grafo):
#   Agregamos el nodo inicial a la cola
    cola.append(nodo_inicial)


    while len(cola) > 0:
#       Agregamos sus nodos adyacentes a la cola
        for adyacente in grafo[nodo_inicial]:
            cola.append(adyacente)
        
#       Imprimimos el primer elemento y lo quitamos de la cola
        print(cola[0], end = " - ")
        cola.pop(0)

#       Hacemos que el nodo inicial sea el siguiente en la cola
        if(cola):
            nodo_inicial = cola[0]



# Grafo1
grafo1 = {
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


grafo2 = {
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

# Almacena los nodos adyacentes pendientes por visitar
cola = []

bfs(1, grafo1)
# bfs(8, grafo2)