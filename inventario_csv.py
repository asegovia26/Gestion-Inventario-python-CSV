from pathlib import Path
import csv

DIRECTORIO_DATOS = Path("datos")
FICHERO_PRODUCTOS = DIRECTORIO_DATOS / "productos.csv"

CAMPOS = [
    "codigo",
    "nombre",
    "precio",
    "stock"
]

def mostrar_menu():
    print("\n" + "=" * 50)
    print(" GESTOR DE INVENTARIO CSV")
    print("=" * 50)
    print("1. Mostrar todos los productos")
    print("2. Buscar un producto por código")
    print("3. Mostrar productos con poco stock")
    print("4. Calcular el valor del inventario")
    print("5. Salir")
    print("=" * 50)

def cargar_productos():
    """
    Lee el fichero CSV y devuelve una lista
    de diccionarios.
    """
    productos = []

    if not FICHERO_PRODUCTOS.exists():
        print("El fichero de productos no existe.")
        return productos

    try:
        with FICHERO_PRODUCTOS.open(
            "r",
            encoding="utf-8",
            newline=""
        ) as archivo:

            lector = csv.DictReader(
                archivo,
                delimiter=";"
            )

            for producto in lector:
                productos.append(producto)

    except OSError as error:
        print(f"No se pudo leer el fichero: {error}")

    except csv.Error as error:
        print(f"El CSV tiene un formato incorrecto: {error}")

    return productos

def mostrar_productos(productos):
    """Muestra todos los productos."""
    if not productos:
        print("No hay productos disponibles.")
        return

    print("\n--- PRODUCTOS ---")

    for producto in productos:
        print(
            f"{producto['codigo']} | "
            f"{producto['nombre']} | "
            f"{producto['precio']} euros | "
            f"Stock: {producto['stock']}"
        )

def buscar_producto(productos):
    """Busca un producto por su código."""
    codigo_buscado = input(
        "Código del producto: "
    ).strip().upper()

    for producto in productos:
        if producto["codigo"].upper() == codigo_buscado:
            print("\nProducto encontrado:")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']} euros")
            print(f"Stock: {producto['stock']}")
            return

    print("No se encontró el producto.")

def mostrar_poco_stock(productos):
    """Muestra productos con menos de 5 unidades."""
    print("\n--- PRODUCTOS CON POCO STOCK ---")

    encontrados = 0

    for producto in productos:
        try:
            stock = int(producto["stock"])

            if stock < 5:
                print(
                    f"{producto['codigo']} | "
                    f"{producto['nombre']} | "
                    f"Stock: {stock}"
                )
                encontrados += 1

        except ValueError:
            print(
                f"Stock incorrecto en el producto "
                f"{producto['codigo']}."
            )

    if encontrados == 0:
        print("No hay productos con poco stock.")

def calcular_valor_inventario(productos):
    """Calcula el valor económico del inventario."""
    valor_total = 0

    for producto in productos:
        try:
            precio = float(producto["precio"])
            stock = int(producto["stock"])

            valor_total += precio * stock

        except ValueError:
            print(
                f"Datos numéricos incorrectos en "
                f"{producto['codigo']}."
            )

    print(
        f"Valor total del inventario: "
        f"{valor_total:.2f} euros"
    )

def ejecutar_opcion(opcion, productos):
    opciones = {
        "1": mostrar_productos,
        "2": buscar_producto,
        "3": mostrar_poco_stock,
        "4": calcular_valor_inventario
    }

    funcion = opciones.get(opcion)

    if funcion is None:
        print("Opción incorrecta.")
        return

    funcion(productos)

def main():
    productos = cargar_productos()

    while True:
        mostrar_menu()

        opcion = input(
            "Selecciona una opción: "
        ).strip()

        if opcion == "5":
            print("Aplicación finalizada.")
            break

        ejecutar_opcion(opcion, productos)

    input("\nPulsa Enter para continuar...")

if __name__ == "__main__":
    main()