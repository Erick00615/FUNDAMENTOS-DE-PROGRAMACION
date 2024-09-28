#Tarea: Trabajando con Diccionarios en Python
#Objetivo: Utilizar diccionarios en Python para representar información estructurada y realizar operaciones comunes.
#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".

# Ejemplo con Diccionarios
informacion_personal = {
    "nombre": "Erick Sarchi",
    "edad": 24,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Imprimir los valores
print("\nInformacion personal:")
print("nombre :", informacion_personal["nombre"])
print("edad :", informacion_personal["edad"])
print("ciudad :", informacion_personal["ciudad"])
print("profesion :", informacion_personal["profesion"])

# Modificar el valor de la clave 'ciudad'
print("\nModificando la ciudad:")
informacion_personal["ciudad"] = "Guayaquil"
print("nombre :", informacion_personal["nombre"])
print("edad :", informacion_personal["edad"])
print("ciudad :", informacion_personal["ciudad"])
print("profesion :", informacion_personal["profesion"])


# Agregar una nueva clave-valor 'telefono' si no existe
print("\nVerificando si existe la clave 'telefono':")
informacion_personal["telefono"] = "098765666555"
print("Clave 'telefono' añadida:" , informacion_personal)

# Eliminar la clave 'edad' del diccionario
print("\nEliminando la clave 'edad':")
del informacion_personal ["edad"]
print("Clave 'edad' eliminada:", informacion_personal)

# Imprimir el diccionario final
print("\nDiccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave} : {valor}")
