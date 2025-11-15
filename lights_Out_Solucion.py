def resolver_lights_out(tablero):
    n = len(tablero)             
    total_celdas = n * n           

    estado_inicial = [tablero[i][j] for i in range(n) for j in range(n)]

    A = [[0] * total_celdas for _ in range(total_celdas)]

    def convertir_a_indice(i, j):
        return i * n + j

    for i in range(n):
        for j in range(n):
            celda = convertir_a_indice(i, j)

            A[celda][celda] = 1

            if i > 0:     A[celda][convertir_a_indice(i-1, j)] = 1
            if i < n-1:   A[celda][convertir_a_indice(i+1, j)] = 1
            if j > 0:     A[celda][convertir_a_indice(i, j-1)] = 1
            if j < n-1:   A[celda][convertir_a_indice(i, j+1)] = 1

    for i in range(total_celdas):
        A[i].append(estado_inicial[i])


    fila_actual = 0
    for columna in range(total_celdas):

        if A[fila_actual][columna] == 0:
            for f in range(fila_actual + 1, total_celdas):
                if A[f][columna] == 1:
                    A[fila_actual] = [(A[fila_actual][c] ^ A[f][c]) for c in range(total_celdas + 1)]
                    break

        if A[fila_actual][columna] == 0:
            continue

        for f in range(fila_actual + 1, total_celdas):
            if A[f][columna] == 1:
                A[f] = [(A[f][c] ^ A[fila_actual][c]) for c in range(total_celdas + 1)]

        fila_actual += 1
        if fila_actual == total_celdas:
            break

    solucion = [0] * total_celdas

    for i in range(total_celdas - 1, -1, -1):
        columna_pivote = None

        for j in range(total_celdas):
            if A[i][j] == 1:
                columna_pivote = j
                break

        if columna_pivote is None:
            continue

        termino_independiente = A[i][total_celdas]

        for j in range(columna_pivote + 1, total_celdas):
            termino_independiente ^= (A[i][j] & solucion[j])

        solucion[columna_pivote] = termino_independiente

    return solucion


tablero = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

resultado = resolver_lights_out(tablero)
print("Solución encontrada:", resultado)