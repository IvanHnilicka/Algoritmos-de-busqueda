def minmax(nodo, grafo, utilidades, profundidad, turnoMax):
    if profundidad == 0 or not grafo[nodo]:
        return utilidades[nodo]
    
    if turnoMax:
        valor_max = -999999999
        for adyacente in grafo[nodo]:
            valor = minmax(adyacente, grafo, utilidades, profundidad - 1, False)
            valor_max = max(valor_max, valor)
        print("Valor maximo: ", valor_max)
        return valor_max
    else:
        valor_min = 999999999
        for adyacente in grafo[nodo]:
            valor = minmax(adyacente, grafo, utilidades, profundidad - 1, True)
            valor_min = min(valor_min, valor)
        print("Valor minimo: ", valor_min)
        return valor_min
    


grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
}

utilidad1 = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': -1,
    'I': 4,
    'J': 2,
    'K': 6,
    'L': -3,
    'M': -5,
    'N': 0,
    'O': 7
}


utilidad2 = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 1,
    'I': 1,
    'J': 2,
    'K': -3,
    'L': 5,
    'M': 7,
    'N': -2,
    'O': -4
}



# print("\nValor optimo: ", minmax('A', grafo, utilidad1, 3, True))
print("\nValor optimo: ", minmax('A', grafo, utilidad2, 3, True))