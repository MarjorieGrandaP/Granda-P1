#Primero, crearemos una función llamada calcular_descuento que tomará dos parámetros:
# el monto total de la compra y un porcentaje de descuento que tendrá un valor predeterminado del 25%.
def calcular_descuento(monto_total, porcentaje_descuento=25):
    # Calcular el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Devolver el monto del descuento
    return descuento
#Segundo, Ahora, en el programa principal, llamaremos a la función calcular_descuento dos veces:
# una vez proporcionando solo el monto total y otra vez proporcionando tanto el monto total
# como el porcentaje de descuento.
# Programa principal
def main():
    # Primer caso: solo monto total
    monto1 = 1000  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)  # Llamada a la función con el descuento predeterminado
    monto_final1 = monto1 - descuento1  # Calcular el monto final a pagar
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento aplicado: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segundo caso: monto total y porcentaje de descuento
    monto2 = 500  # Monto total de la compra
    porcentaje_descuento2 = 15  # Porcentaje de descuento específico
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)  # Llamada a la función con un porcentaje específico
    monto_final2 = monto2 - descuento2  # Calcular el monto final a pagar
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento aplicado: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
print("El descuento aplicado a tu compra fue del 25%")