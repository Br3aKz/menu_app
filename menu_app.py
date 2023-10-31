def agregar_compra(compras):
    precio = float(input("Ingrese el monto de la compra: "))
    compras.append((precio))
    print(f"compra agregada correctamente.")


def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i, (producto, precio) in enumerate(compras, start=1):
            print(f"Compra {i}: {producto} - ${precio}")


def mostrar_total(compras):
    total = sum(compras)
    print(f"Total gastado: ${total:.2f}")

def main():
    compras = []

    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_compra(compras)
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            mostrar_total(compras)
        elif opcion == '4':
            break
        else:
            print("Compra no valida, ingrese otra.")


if __name__ == "__main__":
    main()