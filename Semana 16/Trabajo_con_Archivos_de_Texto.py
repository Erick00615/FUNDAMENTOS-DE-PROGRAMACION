# Trabajo con Archivos de Texto en Python

# 1. Escritura de Archivo de Texto
# Crear un nuevo archivo llamado my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribir al menos tres líneas de notas personales en el archivo
    file.write("Nota 1: Recuerda estudiar para el examen de Programacion.\n")
    file.write("Nota 2: Hacer los deberes despues del trabajo.\n")
    file.write("Nota 3: Llamar a mi madre el fin de semana.\n")

# 2. Lectura de Archivo de Texto
# Abrir el archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leer el contenido del archivo línea por línea
    for line in file:
        # Mostrar en la consola cada línea leída
        print(line.strip())  # strip() elimina los espacios en blanco al inicio y al final

# 3. Cierre de Archivos
# Los archivos se cierran automáticamente al salir del bloque 'with'