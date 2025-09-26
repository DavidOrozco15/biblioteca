# Sistema de Gestión de Biblioteca Personal
# Este programa utiliza solo diccionarios, tuplas, funciones, if, while, match,
# estructuras condicionales y operadores normales/lógicos, como se solicitó.
# No se usan listas, sets u otras estructuras avanzadas.

# Diccionario principal para almacenar la biblioteca
# Clave: ID único (entero), Valor: tupla (titulo, autor, genero, año, estado)
biblioteca = {}
contador_id = 1  # Contador para generar IDs únicos

# Función para agregar un libro
def agregar_libro():
    global contador_id
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    try:
        año = int(input("Ingrese el año de publicación: "))
    except ValueError:
        print("Error: El año debe ser un número entero.")
        return
    estado = input("Ingrese el estado (leído/no leído): ").lower()
    if estado not in ['leído', 'no leído']:
        print("Error: El estado debe ser 'leído' o 'no leído'.")
        return
    
    # Crear tupla con la información
    libro = (titulo, autor, genero, año, estado)
    biblioteca[contador_id] = libro
    print(f"Libro agregado con ID: {contador_id}")
    contador_id += 1

# Función para mostrar todos los libros
def ver_biblioteca():
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    print("\n--- Biblioteca Completa ---")
    for id_libro, info in biblioteca.items():
        titulo, autor, genero, año, estado = info
        print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
    print("---------------------------")

# Función para buscar libros
def buscar_libros():
    if not biblioteca:
        print("La biblioteca está vacía.")
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
            return
        
        if coincidencia:
            print(f"ID: {id_libro} | Título: {titulo} | Autor: {autor} | Género: {genero} | Año: {año} | Estado: {estado}")
            encontrados = True
    
    if not encontrados:
        print("No se encontraron libros que coincidan con la búsqueda.")

# Función para cambiar el estado de lectura
def cambiar_estado():
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    if id_libro not in biblioteca:
        print("ID no encontrado.")
        return
    
    nuevo_estado = input("Nuevo estado (leído/no leído): ").lower()
    if nuevo_estado not in ['leído', 'no leído']:
        print("Error: El estado debe ser 'leído' o 'no leído'.")
        return
    
    # Actualizar la tupla (crear nueva tupla ya que las tuplas son inmutables)
    titulo, autor, genero, año, _ = biblioteca[id_libro]
    biblioteca[id_libro] = (titulo, autor, genero, año, nuevo_estado)
    print("Estado actualizado correctamente.")

# Función para generar estadísticas
def estadisticas():
    if not biblioteca:
        print("La biblioteca está vacío.")
        return
    
    total_libros = len(biblioteca)
    leidos = 0
    por_leer = 0
    generos = {}  # Diccionario temporal para contar géneros
    
    for info in biblioteca.values():
        _, _, genero, _, estado = info
        if estado == 'leído':
            leidos += 1
        else:
            por_leer += 1
        
        # Contar géneros
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1
    
    print(f"\n--- Estadísticas ---")
    print(f"Total de libros: {total_libros}")
    print(f"Libros leídos: {leidos}")
    print(f"Libros por leer: {por_leer}")
    
    if generos:
        print("Géneros más frecuentes:")
        # Encontrar el género con más apariciones (iterar manualmente)
        max_count = 0
        genero_max = ""
        for g, count in generos.items():
            if count > max_count:
                max_count = count
                genero_max = g
        print(f"Género más frecuente: {genero_max} ({max_count} libros)")
    print("--------------------")

# Función para eliminar un libro
def eliminar_libro():
    if not biblioteca:
        print("La biblioteca está vacía.")
        return
    
    try:
        id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return
    
    if id_libro not in biblioteca:
        print("ID no encontrado.")
        return
    
    # Mostrar info para confirmar
    titulo, autor, genero, año, estado = biblioteca[id_libro]
    confirm = input(f"¿Eliminar '{titulo}' de {autor}? (s/n): ").lower()
    if confirm == 's':
        del biblioteca[id_libro]
        print("Libro eliminado correctamente.")
    else:
        print("Eliminación cancelada.")

# Programa principal con menú
def main():
    while True:
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
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
