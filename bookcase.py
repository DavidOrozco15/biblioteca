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
    print("\n----AGREGAR LIBRO----")
    titulo = input("\nIngrese el título del libro: ")
    autor = input("\nIngrese el autor del libro: ")
    genero = input("\nIngrese el género del libro: ")
    try:
        año = int(input("\nIngrese el año de publicación: "))
    except ValueError:
        print("\nError: El año debe ser un número entero.")
        pausar()
        return
    
    estado = input("\n¿Ya lo leíste? (s/n): ").lower()
    if estado == 's':
        estado = "✅"
    elif estado == 'n':
        estado = "❌"
    else:
        print("\nError: Debe responder 's' para sí o 'n' para no.")
        pausar()
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
        print("\nLa biblioteca está vacía.")
        pausar()
        return
    print("\n----------------------------------------Biblioteca Completa-----------------------------------------------")
    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        print(f"\nID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
    print("------------------------------------------------------------------------------------------------------------")
    pausar()

# Función para buscar libros
def buscar_libros():
    limpiar()
    if not biblioteca:
        print("\nLa biblioteca está vacía.")
        pausar()
        return
    print("----BUSCAR LIBRO----")
    buscarPor = input("\nBuscar por | 1: Título | 2: Autor | 3: Género |: ")
    termino = input("\nIngrese el término de búsqueda: ").lower()
    
    encontrados = False  # ✅ se inicializa una sola vez
    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        siEncontro = False  # ✅ se resetea por libro
        
        if buscarPor == '1':
            if termino in titulo.lower():
                siEncontro = True
        elif buscarPor == '2':
            if termino in autor.lower():
                siEncontro = True
        elif buscarPor == '3':
            if termino in genero.lower():
                siEncontro = True
        else:
            print("Indice inválido.")
            pausar()
            return
        
        if siEncontro:
            print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
            encontrados = True   # ✅ ahora sí se mantiene en True si encuentra algo
    
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
        print("\n--- Biblioteca Completa ---")
        for id_libro, info in biblioteca.items():
            titulo, autor, genero, año, estado = info
            print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
        print("---------------------------")
        id_libro = int(input("Ingrese el ID del libro: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        pausar()
        return
    
    if id_libro not in biblioteca:
        print("ID no encontrado.")
        pausar()
        return
    
    
    entrada = input("¿Ya lo leíste? (s/n): ").lower()
    if entrada == 's':
        nuevoEstado = "✅"
    elif entrada == 'n':
        nuevoEstado = "❌"
    else:
        print("Error: Debe responder 's' o 'n'.")
        pausar()
        return
    
    # Actualizar la tupla
    titulo, autor, genero, año, _ = biblioteca[id_libro]
    biblioteca[id_libro] = (titulo, autor, genero, año, nuevoEstado)
    print("Estado actualizado correctamente.")
    pausar()

# Función para generar estadísticas
def estadisticas():
    limpiar()
    if not biblioteca:
        print("La biblioteca está vacía.")
        pausar()
        return
    
    totalLibros = len(biblioteca)
    leidos = 0
    noLeidos = 0
    generos = {}
    
    for info in biblioteca.values():
        _, _, genero, _, estado = info
        if estado == "✅":
            leidos += 1
        else:
            noLeidos += 1
        
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1
    
    print(f"\n--- Estadísticas ---")
    print(f"Total de libros: {totalLibros}")
    print(f"Libros leídos (✅): {leidos}")
    print(f"Libros por leer (❌): {noLeidos}")
    
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
    
    titulo, autor, _, _, _ = biblioteca[id_libro]
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
        print()
        print("1. Agregar libro")
        print("2. Ver biblioteca completa")
        print("3. Buscar libros")
        print("4. Cambiar estado de lectura")
        print("5. Ver estadísticas")
        print("6. Eliminar libro")
        print("7. Salir")
        print()
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