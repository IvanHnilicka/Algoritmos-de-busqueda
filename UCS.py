def ucs(nodo_inicial, grafo):
    nodo_actual = [nodo_inicial, 0]
    pila.append(nodo_actual)
    visitados.append(nodo_actual)

#   Almacena los posibles caminos desde el nodo inicial en la cola
    for adyacente in grafo[nodo_inicial]:
        cola.append(adyacente)


#   Seguimos explorando mientras haya caminos disponibles en la cola
    while(cola):
#       Busca el camino de menor costo
        costo_minimo = 999999999
        for i in range(0, len(cola)):
            if cola[i][1] < costo_minimo:
                costo_minimo = cola[i][1]
                nodo_actual = cola[i]
            
#       Removemos el nodo con menor costo de la cola debido a que ya se visitó
        cola.pop(cola.index(nodo_actual))
            
#       Agregamos a la cola los caminos adyacentes del nodo visitado
        for adyacente in grafo[nodo_actual[0]]:
            cola.append(adyacente)
        
#       Si el actual no es adyacente al ultimo de la ruta lo quitamos de la ruta
        while not grafo[pila[-1][0]].count(nodo_actual):
            pila.pop(-1)

            if not pila:
                nodo = nodo_actual
                for i in range(len(visitados) - 1, 0):
                    if grafo[visitados[i][0]].count(nodo):
                        pila.insert(0, nodo)
                        nodo = visitados[i]
                pila.append(nodo)
                

        pila.append(nodo_actual)
        visitados.append(nodo_actual)

        print("Nodo actual: ", nodo_actual)       
        print("Cola: ", cola)
        print("Pila: ", pila)
        print("Visitados: ", visitados, "\n")




grafo = {
#   Nodo: [[adyacente, costo]]
    1: [
        [2, 1], 
        [3, 4]
       ],

    2: [
        [4, 3], 
        [5, 2]
       ],

    3: [
        [6, 5]
       ],

    4: [
        [7, 5]
       ],

    5: [
        [8, 2], 
        [6, 3]
       ],

    6: [],
    
    7: [
        [6, 5]
       ],

    8: []
}


# Almacena los caminos disponibles para poder escoger el de menor costo
cola = []
pila = []
visitados = []

ucs(1, grafo)