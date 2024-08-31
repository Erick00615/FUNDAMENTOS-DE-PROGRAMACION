# Programa 2: Ordenación de Arreglo Multidimensional

# Definir la matriz 3x3
matriz = [
    [9, 3, 7],
    [4, 5, 6],
    [8, 2, 1]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar los elementos
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 0 (primera fila)
ordenar_fila(matriz, 0)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la primera fila ordenada:")
for fila in matriz:
    print(fila)