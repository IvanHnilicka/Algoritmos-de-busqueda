def ucs(nodo_inicial, grafo, nodo_objetivo):
    nodo_actual = [nodo_inicial, 0]
    pila.append(nodo_actual)
    visitados.append(nodo_actual)

#   Almacena los posibles caminos desde el nodo inicial en la cola
    for adyacente in grafo[nodo_inicial]:
        cola.append(adyacente)    


#   Seguimos explorando mientras haya caminos disponibles en la cola
    while cola:
#       Busca el camino de menor costo
        costo_minimo = 999999999
        for i in range(0, len(cola)):
            if cola[i][1] <= costo_minimo:
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

#           Si la pila se queda vacía generamos el camino hasta llegar al nodo actual
            if not pila:
                nodo = nodo_actual
#               Checamos los nodos visitados para generar el camino hacia atrás a partir de ellos                          
                for i in range(len(visitados) - 1, -1, -1):
#                   Si el nodo que se esta checando es adyacente lo agregamos al principio de la pila                    
                    if grafo[visitados[i][0]].count(nodo):
                        nodo = visitados[i]
                        pila.insert(0, nodo)
                break


        pila.append(nodo_actual)
        visitados.append(nodo_actual)

#       Si el nodo actual es el nodo objetivo calculamos el costo de la ruta actual
        if(nodo_actual[0] == nodo_objetivo):
            costo_actual = 0
            print("\nRuta: ", end = "")
            for i in range(0, len(pila)):
                costo_actual += pila[i][1]
                if i != len(pila) - 1:
                    print(pila[i][0], end = " - ")
                else:
                    print(pila[i][0])

            print("Costo de ruta: ", costo_actual)



grafoCostos1 = {
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


grafoCostos2 = {
    1: [
        [2, 1], 
        [3, 2]
    ],
    2: [
        [4, 4], 
        [5, 5]
    ],
    3: [
        [5, 3]
    ],
    4: [
        [6, 4]
    ],
    5: [
        [6, 3]
    ],
    6: []
}



# Almacena los caminos disponibles para poder escoger el de menor costo
cola = []

# Almacena la ruta actual que se está siguiendo
pila = []

# Almacena los nodos que ya fueron visitados
visitados = []


ucs(1, grafoCostos1, 6)
# ucs(1, grafoCostos2, 6)