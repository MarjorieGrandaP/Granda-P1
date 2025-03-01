print ("""Bienvenido, a continuación se muestra la búsqueda en una 
arreglo bidimensionals""")
# Definimos la matriz bidimensional de 3x3
matriz = [
    [5, 8, 3],
    [1, 7, 9],
    [4, 6, 2]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    # Recorremos la matriz fila por fila
    for i in range(len(matriz)):  # i es el índice de la fila
        for j in range(len(matriz[i])):  # j es el índice de la columna
            if matriz[i][j] == valor:
                return (i, j)  # Retornamos la posición si se encuentra el valor
    return None  # Retornamos None si no se encuentra el valor

# Valor a buscar
valor_a_buscar = 7

# Llamamos a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostramos los resultados
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")