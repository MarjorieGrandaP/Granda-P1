
print ("""A continuación se muestra el promedio de las temperaturas más bajas
que alcanzaron algunas ciudades del país en el mes de febrero de 2025 desde 
el lunes 03 al domingo 23 de febrero""")
def calcular_temperatura_promedio(temperaturas):
    # Inicializamos diccionarios para almacenar los promedios semanales y mensuales
    promedios_semanales = {}
    promedios_mensuales = {}

    # Iteramos sobre cada ciudad y sus temperaturas
    for ciudad, temps in temperaturas.items():
        # Asegurarse de que hay exactamente 28 días de datos (4 semanas)
        if len(temps) != 28:
            raise ValueError(f"Se requieren 28 días de datos para {ciudad}.")

        # Dividir las temperaturas en 4 semanas (7 días cada una)
        semanas = [temps[i:i + 7] for i in range(0, len(temps), 7)]

        # Calcular el promedio de temperatura para cada semana
        promedios_semanales[ciudad] = [sum(semana) / len(semana) for semana in semanas]

        # Calcular el promedio mensual sumando todas las temperaturas y dividiendo por el total de días
        promedios_mensuales[ciudad] = sum(temps) / len(temps)

    # Retornar los promedios semanales y mensuales
    return promedios_semanales, promedios_mensuales


# Ejemplo de uso
temperaturas_febrero = {
    'Loja': [26, 25, 26, 25, 25, 25, 25,  # Semana 1
             25, 26, 25, 25, 24, 23, 23,   # Semana 2
             24, 24, 23, 25, 24, 24, 25,  # Semana 3
             24, 24, 24, 24, 26, 24, 26],  # Semana 4

    'Machala': [25, 26, 25, 25, 24, 23, 23,  # Semana 1
                24, 24, 23, 25, 24, 24, 25,  # Semana 2
                24, 24, 24, 25, 25, 24, 24,  # Semana 3
                24, 24, 24, 24, 26, 24, 26],  # Semana 4

    'Cuenca': [25, 26, 25, 25, 24, 23, 23,  # Semana 1
               24, 24, 23, 25, 24, 24, 25,  # Semana 2
               24, 24, 24, 25, 25, 24, 24,  # Semana 3
               24, 24, 24, 24, 26, 24, 26]  # Semana 4
}

# Llamar a la función con los datos de temperatura y almacenar los resultados
promedios_semanales, promedios_mensuales = calcular_temperatura_promedio(temperaturas_febrero)

# Imprimir los promedios semanales de forma vertical
print("Promedios Semanales:")
for ciudad, promedios in promedios_semanales.items():
    print(f"{ciudad}:")
    for i, promedio in enumerate(promedios, start=1):
        print(f"  Promedio de la temperatura en la semana {i}: {promedio:.2f}")

# Imprimir los promedios mensuales
print("\nPromedios Mensuales:")
for ciudad, promedio in promedios_mensuales.items():
    print(f"{ciudad}: {promedio:.2f}")
