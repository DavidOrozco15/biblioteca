import os


biblioteca = {}
contadorId = 1  # Contador para generar IDs únicos

def limpiar():
    os.system("clear")

def pausar():
    input("\nPresiona enter para continuar......")


# Función para agregar un libro
def agregar_libro():
    global contadorId
    limpiar()
    print("----AGREGAR LIBRO----")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    try:
        año = int(input("Ingrese el año de publicación: "))
    except ValueError:
        print("Error: El año debe ser un número entero.")
        return
    
    estado = input("¿Ya lo leíste? (s/n): ").lower()
    if estado == 's':
        estado = "✅"
    elif estado == 'n':
        estado = "❌"
    else:
        print("Error: Debe responder 's' para sí o 'n' para no.")
        return
    
    # Crear tupla con la información
    libro = (titulo, autor, genero, año, estado)
    biblioteca[contadorId] = libro
    print(f"\nLibro agregado con ID: {contadorId}")
    contadorId += 1
    pausar()

# Función para mostrar todos los libros
def ver_biblioteca():
    limpiar()
    print("----CONTENIDO DE LA BIBLIOTECA----")
    if not biblioteca:
        print("La biblioteca está vacía.")
        pausar()
        return
    print("\n--- Biblioteca Completa ---")
    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
    print("---------------------------")
    pausar()

# Función para buscar libros
def buscar_libros():
    limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        pausar()
        return
    
    criterio = input("Buscar por (1: Título, 2: Autor, 3: Género): ")
    busqueda = input("Ingrese el término de búsqueda: ").lower()
    
    encontrados = False
    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        coincidencia = False
        
        if criterio == '1':
            if busqueda in titulo.lower():
                coincidencia = True
        elif criterio == '2':
            if busqueda in autor.lower():
                coincidencia = True
        elif criterio == '3':
            if busqueda in genero.lower():
                coincidencia = True
        else:
            print("Criterio inválido.")
            pausar()
            return
        
        if coincidencia:
            print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
            encontrados = True
            pausar()
    
    if not encontrados:
        print("No se encontraron libros que coincidan con la búsqueda.")
        pausar()

# Función para cambiar el estado de lectura
def cambiar_estado():
    limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        pausar()
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        pausar()
        return
    
    if id_libro not in biblioteca:
        print("ID no encontrado.")
        pausar()
        return
    
    nuevo_estado_input = input("¿Ya lo leíste? (s/n): ").lower()
    if nuevo_estado_input == 's':
        nuevo_estado = "✅"
    elif nuevo_estado_input == 'n':
        nuevo_estado = "❌"
    else:
        print("Error: Debe responder 's' o 'n'.")
        pausar()
        return
    
    # Actualizar la tupla
    titulo, autor, genero, año, _ = biblioteca[id_libro]
    biblioteca[id_libro] = (titulo, autor, genero, año, nuevo_estado)
    print("Estado actualizado correctamente.")
    pausar()

# Función para generar estadísticas
def estadisticas():
    limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        pausar()
        return
    
    total_libros = len(biblioteca)
    leidos = 0
    por_leer = 0
    generos = {}
    
    for info in biblioteca.values():
        _, _, genero, _, estado = info
        if estado == "✅":
            leidos += 1
        else:
            por_leer += 1
        
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1
    
    print(f"\n--- Estadísticas ---")
    print(f"Total de libros: {total_libros}")
    print(f"Libros leídos (✅): {leidos}")
    print(f"Libros por leer (❌): {por_leer}")
    
    if generos:
        print("Géneros más frecuentes:")
        max_count = 0
        genero_max = ""
        for g, count in generos.items():
            if count > max_count:
                max_count = count
                genero_max = g
        print(f"Género más frecuente: {genero_max} ({max_count} libros)")
    print("--------------------")
    pausar()

# Función para eliminar un libro
def eliminar_libro():
    limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        pausar()
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        pausar()
        return
    
    if id_libro not in biblioteca:
        print("ID no encontrado.")
        pausar()
        return
    
    titulo, autor, genero, año, estado = biblioteca[id_libro]
    confirm = input(f"¿Eliminar '{titulo}' de {autor}? (s/n): ").lower()
    if confirm == 's':
        del biblioteca[id_libro]
        print("Libro eliminado correctamente.")
        pausar()
    else:
        print("Eliminación cancelada.")
        pausar()

# Programa principal con menú
def main():
    while True:
        limpiar()
        print("\n--- Menú de Biblioteca ---")
        print("1. Agregar libro")
        print("2. Ver biblioteca completa")
        print("3. Buscar libros")
        print("4. Cambiar estado de lectura")
        print("5. Ver estadísticas")
        print("6. Eliminar libro")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case '1':
                agregar_libro()
            case '2':
                ver_biblioteca()
            case '3':
                buscar_libros()
            case '4':
                cambiar_estado()
            case '5':
                estadisticas()
            case '6':
                eliminar_libro()
            case '7':
                print("¡Hasta luego! 👋")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()