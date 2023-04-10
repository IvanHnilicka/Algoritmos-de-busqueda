def ids():
    limite = int(input("Ingrese el numero de iteraciones a realizar: "))

    for i in range(0, limite):
        visitados = { nodo: False for nodo in grafo }
        print("\n--------------------------------------")
        print("\tIteración ", str(i + 1))
        print("--------------------------------------")
        dls(1, visitados, grafo, 0, i)


def dls(nodo, visitados, grafo, cuenta, limite):
#   Indica cuantas iteraciones se han hecho
    contador = cuenta
    
#   Mientras no pasemos el limite seguimos explorando el grafo
    if contador <= limite:

#       Marcamos el nodo actual como visitado
        visitados[nodo] = True
        print(nodo)

#       Llamamos a la función con cada uno de los nodos adyacentes que no hayan sido visitados
        for adyacente in grafo[nodo]:
            if not visitados[adyacente]:
                dls(adyacente, visitados, grafo, contador + 1, limite)


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

ids()