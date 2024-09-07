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

# Iterar y calcular promedios de temperaturas por ciudad y semana
for ciudad, semanas in temperaturas.items():
    print(f"\nCiudad: {ciudad}")
    for semana_index, semana in enumerate(semanas):
        suma_temperaturas = 0
        for dia in semana:
            suma_temperaturas += dia["temp"]
        promedio = suma_temperaturas / len(semana)
        print(f"Semana {semana_index + 1}: Promedio de temperatura = {promedio:.2f}°C")