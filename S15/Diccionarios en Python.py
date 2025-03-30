# 1. Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Juan Alcantara",
    "edad": 30,  # Esta clave será eliminada
    "ciudad": "Riobamba",  # Valor inicial que será modificado
    "profesion": "Ingeniero"
}

# 2. Acceder y modificar el valor de la clave "ciudad" a "Quito"
informacion_personal["ciudad"] = "Quito"  # Cambiamos Riobamba por Quito

# 3. Agregar una nueva clave-valor para la "provincia"
informacion_personal["provincia"] = "Pichincha"  # Añadimos la provincia

# 4. Agregar una nueva clave-valor para el "país"
informacion_personal["pais"] = "Ecuador"  # Añadimos el país

# 5. Verificar si la clave "telefono" existe, y agregarla si no
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985124774"  # Agregamos un teléfono ficticio

# 6. Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminamos la clave "edad" porque no es necesaria

# Imprimir el diccionario
print("Diccionario Final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# Mensaje sobre las modificaciones realizadas
print("\nModificaciones realizadas:")
print("- Se cambió la ciudad de 'Riobamba' a 'Quito'.")
print("- Se agregó la provincia 'Pichincha'.")
print("- Se agregó el país 'Ecuador'.")
print("- Se eliminó la clave 'edad' porque no es necesaria.")