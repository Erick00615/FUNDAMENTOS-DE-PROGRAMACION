"""Crea una función llamada calcular_descuento que tome dos parámetros:
El monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
La función debe devolver el monto del descuento calculado.
Llama a la función calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento."""

# Función para calcular el descuento

def calcular_descuento(monto_total, porcentaje_descuento=10):

    # Calculamos el monto del descuento como un porcentaje del monto total
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

def main():
    # Primer ejemplo de monto total
    monto1 = 200
    # Llamamos a la función calcular_descuento con el monto total y usamos el porcentaje de descuento
    descuento1 = calcular_descuento(monto1)
    # Calculamos el monto final a pagar después del descuento
    monto_final1 = monto1 - descuento1
    print(f"Para un monto de {monto1}, el descuento es de: {descuento1}" )
    print(f"El valor final a pagar es: {monto_final1}")

    # Segundo ejemplo de monto total y un porcentaje
    monto2 = 500
    porcentaje2 = 15
    # Llamamos a la función calcular_descuento con el monto total y el porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    # Calculamos el monto final a pagar después del descuento
    monto_final2 = monto2 - descuento2
    print(f"Para un monto de {monto2} con un descuento del {porcentaje2}%, el descuento es de: {descuento2} ")
    print(f"El valor final a pagar es: {monto_final2}")

# Verificamos que este archivo es el programa principal que se está ejecutando
if __name__ == "__main__":
    main()