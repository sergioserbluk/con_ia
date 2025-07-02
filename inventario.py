"""Sistema de inventario para materiales de construcción."""

# Lista principal que almacena los materiales como diccionarios
inventario = []


def buscar_material_por_id(material_id):
    """Devuelve el índice de un material por su identificador."""
    for i, material in enumerate(inventario):
        if material["id"] == material_id:
            return i
    return None


def agregar_material():
    """Registra un nuevo material asegurando que el ID sea único."""
    try:
        material_id = int(input("ID del material: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return

    if buscar_material_por_id(material_id) is not None:
        print("Ya existe un material con ese ID.")
        return

    nombre = input("Nombre del material: ")
    try:
        cantidad = int(input("Cantidad inicial: "))
    except ValueError:
        print("La cantidad debe ser numérica.")
        return

    inventario.append({"id": material_id, "nombre": nombre, "cantidad": cantidad})
    print("Material agregado con éxito.")


def listar_materiales():
    """Muestra todos los materiales registrados."""
    if not inventario:
        print("Inventario vacío.")
    else:
        for m in inventario:
            print(f"ID: {m['id']} | Nombre: {m['nombre']} | Cantidad: {m['cantidad']}")


def actualizar_material():
    """Actualiza la cantidad de un material existente."""
    try:
        material_id = int(input("ID del material a actualizar: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return

    idx = buscar_material_por_id(material_id)
    if idx is None:
        print("Material no encontrado.")
        return

    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
    except ValueError:
        print("La cantidad debe ser numérica.")
        return

    inventario[idx]["cantidad"] = nueva_cantidad
    print("Cantidad actualizada.")


def eliminar_material():
    """Elimina un material del inventario por ID."""
    try:
        material_id = int(input("ID del material a eliminar: "))
    except ValueError:
        print("El ID debe ser numérico.")
        return

    idx = buscar_material_por_id(material_id)
    if idx is None:
        print("Material no encontrado.")
    else:
        inventario.pop(idx)
        print("Material eliminado.")


def buscar_material():
    """Busca un material por ID o por nombre."""
    criterio = input("Buscar por (id/nombre): ").strip().lower()
    if criterio == "id":
        try:
            material_id = int(input("ID del material: "))
        except ValueError:
            print("El ID debe ser numérico.")
            return
        idx = buscar_material_por_id(material_id)
        if idx is None:
            print("Material no encontrado.")
        else:
            m = inventario[idx]
            print(f"ID: {m['id']} | Nombre: {m['nombre']} | Cantidad: {m['cantidad']}")
    elif criterio == "nombre":
        nombre = input("Nombre del material: ")
        resultados = [m for m in inventario if m["nombre"].lower() == nombre.lower()]
        if resultados:
            for m in resultados:
                print(f"ID: {m['id']} | Nombre: {m['nombre']} | Cantidad: {m['cantidad']}")
        else:
            print("Material no encontrado.")
    else:
        print("Opción de búsqueda no válida.")


def mostrar_menu():
    print("\nInventario de materiales")
    print("1. Agregar material")
    print("2. Listar materiales")
    print("3. Actualizar cantidad")
    print("4. Eliminar material")
    print("5. Buscar material")
    print("6. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_material()
        elif opcion == "2":
            listar_materiales()
        elif opcion == "3":
            actualizar_material()
        elif opcion == "4":
            eliminar_material()
        elif opcion == "5":
            buscar_material()
        elif opcion == "6":
            print("Hasta luego")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
