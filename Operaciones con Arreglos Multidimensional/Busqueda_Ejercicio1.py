# Programa 1: Búsqueda en Arreglo Multidimensional

# Definir la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)
    return None

# Valor a buscar
valor_buscado = 2

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado de la búsqueda
if posicion:
    print(f"Valor {valor_buscado} encontrado en la posición {posicion}")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz")