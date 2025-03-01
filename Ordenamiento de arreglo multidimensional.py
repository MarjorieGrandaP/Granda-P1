print ("""Bienvenido, a continuación se muestra un programa que incluye "
 una matriz bidimensional con valores numéricos en el cual se da el ordenamiento
 de dicho arreglo""")
# Definimos la matriz bidimensional de 3x3
matriz = [
    [3, 2, 1],
    [5, 6, 4],
    [8, 7, 9]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    # Copiamos la fila que queremos ordenar
    fila_a_ordenar = matriz[fila]
    n = len(fila_a_ordenar)

    # Implementación del algoritmo Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                # Intercambiamos los elementos si están en el orden incorrecto
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]

    # Actualizamos la fila ordenada en la matriz original
    matriz[fila] = fila_a_ordenar

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la fila 1 (segunda fila, índice 1)
ordenar_fila(matriz, 1)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)