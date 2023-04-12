def alpha_beta(nodo, grafo, utilidades, profundidad, alpha, beta, turnoMax):
    if profundidad == 0 or not grafo[nodo]:
        return utilidades[nodo]
    
    if turnoMax:
        valor_max = -999999999
        for adyacente in grafo[nodo]:
            valor = alpha_beta(adyacente, grafo, utilidades, profundidad - 1, alpha, beta, False)
            valor_max = max(valor_max, valor)
            alpha = max(alpha, valor_max)

            if beta <= alpha:
                print("Corte despues de nodo ", adyacente)
                break

        print("\nValor maximo: ", valor_max)
        return valor_max
    
    else:
        valor_min = 999999999
        for adyacente in grafo[nodo]:
            valor = alpha_beta(adyacente, grafo, utilidades, profundidad - 1, alpha, beta, True)
            valor_min = min(valor_min, valor)
            beta = min(beta, valor)

            if beta <= alpha:
                print("Corte despues de nodo ", adyacente)
                break

        print("\nValor minimo: ", valor_min)
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
    'H': 2,
    'I': 3,
    'J': 5,
    'K': 9,
    'L': 0,
    'M': 1,
    'N': 7,
    'O': 5
}


print(alpha_beta('A', grafo, utilidad1, 3, -999999999, 999999999, True))