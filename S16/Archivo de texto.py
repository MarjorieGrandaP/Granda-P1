# Escritura de Archivo de Texto

# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres notas personales en el archivo, cada una en una línea diferente
archivo.write("El domingo 13 de Abril debo ir a votar a las 7:00 am para evitar el tráfico y no debo olvidarme la cédula.\n")
archivo.write("El lunes 14 de abril tengo una cita médica en Quito por lo cuál debo salir a las 4:00 am de mi casa.\n")
archivo.write("El martes 15 de abril debo comprar un regalo para el cumpleaños de mi amigo Carlos.\n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura de Archivo de Texto

# Abrimos el archivo 'my_notes.txt' en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el archivo línea por línea usando un bucle
print("Contenido del archivo my_notes.txt:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() elimina saltos de línea extra al imprimir
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
