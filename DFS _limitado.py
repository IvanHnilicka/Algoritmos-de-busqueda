def dls(nodo, visitados, grafo1, cuenta, limite):
#   Indica cuantas iteraciones se han hecho
    contador = cuenta
    
#   Mientras no pasemos el limite seguimos explorando el grafo1
    if contador <= limite:

#       Marcamos el nodo actual como visitado
        visitados[nodo] = True
        print(nodo)

#       Llamamos a la función con cada uno de los nodos adyacentes que no hayan sido visitados
        for adyacente in grafo1[nodo]:
            if not visitados[adyacente]:
                dls(adyacente, visitados, grafo1, contador + 1, limite)



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

visitados = { nodo: False for nodo in grafo1 }


# Limite de iteraciones a realizar
limite = int(input("Ingrese el limite de profundidad: "))
dls(1, visitados, grafo1, 0, limite)
