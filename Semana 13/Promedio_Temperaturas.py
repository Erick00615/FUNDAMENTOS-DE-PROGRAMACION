# Desarrollo de Función para Calcular Temperaturas Promedio de cada ciudad
# Registro de temperaturas diarias por ciudad, semana y día
# Matriz de temperaturas: Quito, Guayaquil y Ambato
# Cada ciudad tiene temperaturas registradas por día durante 4 semanas

temperaturas = {
    "Quito": [
        # Semana 1
        [
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 20}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 21}
        ]
    ],
    "Guayaquil": [
        # Semana 1
        [
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 30}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 31}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 32}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    "Ambato": [
        # Semana 1
        [
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 14},
            {"day": "Domingo", "temp": 17}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 18}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 19}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 18}
        ]
    ]
}


# Función para calcular el promedio de temperaturas de una ciudad específica
def calcular_promedio_temperatura(ciudad):
    # Obtener las semanas de temperaturas de la ciudad seleccionada
    semanas = temperaturas[ciudad]

    # Recorrer cada semana y calcular el promedio de temperatura para esa semana
    for semana_index, semana in enumerate(semanas):
        # Sumar todas las temperaturas de los días de la semana
        suma_temperaturas = sum([dia["temp"] for dia in semana])

        # Calcular el promedio dividiendo la suma de temperaturas por el número de días
        promedio = suma_temperaturas / len(semana)

        # Mostrar el promedio de temperatura para la semana actual
        print(f"Semana {semana_index + 1}: Promedio de temperatura = {promedio:.2f}°C")


# Función principal del programa
def main():
    # Bucle infinito que seguirá pidiendo ciudades hasta que el usuario decida salir
    while True:
        # Mostrar opciones de ciudades y la opción de salir en formato de lista numerada
        print("\nLista de ciudades para obtener su promedio de temperatura :")
        print("1. Quito")
        print("2. Guayaquil")
        print("3. Ambato")
        print("4. Salir")

        # Solicitar al usuario que elija una opción
        opcion = input("Ingrese el número de su opción: ")

        # Procesar la opción seleccionada
        if opcion == '1':
            ciudad_seleccionada = "Quito"
            print(f"\nCalculando promedios para {ciudad_seleccionada}:")
            calcular_promedio_temperatura(ciudad_seleccionada)
        elif opcion == '2':
            ciudad_seleccionada = "Guayaquil"
            print(f"\nCalculando promedios para {ciudad_seleccionada}:")
            calcular_promedio_temperatura(ciudad_seleccionada)
        elif opcion == '3':
            ciudad_seleccionada = "Ambato"
            print(f"\nCalculando promedios para {ciudad_seleccionada}:")
            calcular_promedio_temperatura(ciudad_seleccionada)
        elif opcion == '4':
            # Si el usuario elige la opción de salir, finalizar el programa
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            # Si la opción es inválida, mostrar un mensaje de error
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Llamar a la función principal para iniciar el programa
main()