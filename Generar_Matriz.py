import numpy as np

def generar_matriz_identidad(n):
    matriz_aleatoria = np.random.randint(0, 2, size=(n, n))
    return matriz_aleatoria
print(generar_matriz_identidad(3))
