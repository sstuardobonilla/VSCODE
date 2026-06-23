# ==========================================
# ESTE ES MI TRABAJO DE LOGICA Y DISEÑO DE PROGRAMACION: PROGRAMA DE GESTIÓN DE RECURSOS HUMANOS
# ==========================================

# Creamos una lista vacía para guardar a todos los empleados
lista_empleados = []

# Este bucle 'while' mantendrá el programa funcionando hasta que elijamos salir
ejecutando = True

while ejecutando:
    # 1. MOSTRAR EL MENÚ DE OPCIONES
    print("\n--- MENÚ PRINCIPAL RECURSOS HUMANOS ---")
    print("1. Agregar nuevo empleado")
    print("2. Buscar empleado")
    print("3. Actualizar información de empleado")
    print("4. Eliminar empleado")
    print("5. Salir del programa")
    
    # Pedimos al usuario que elija una opción
    opcion = input("\nSelecciona una opción (1-5): ")
    
    # ---------------------------------------------------------
    # OPCIÓN 1: AGREGAR EMPLEADO
    # ---------------------------------------------------------
    if opcion == "1":
        print("\n--- REGISTRAR NUEVO EMPLEADO ---")
        
        # Pedimos los datos uno por uno
        id_empleado = input("Número de Identificación: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cargo = input("Cargo: ")
        departamento = input("Departamento: ")
        salario = input("Salario: ")
        fecha = input("Fecha de contratación (DD/MM/AAAA): ")
        
        # Creamos un diccionario para este empleado con los datos guardados
        nuevo_empleado = {
            "id": id_empleado,
            "nombre": nombre,
            "apellido": apellido,
            "cargo": cargo,
            "departamento": departamento,
            "salario": salario,
            "fecha": fecha
        }
        
        # Guardamos el diccionario dentro de nuestra lista general
        lista_empleados.append(nuevo_empleado)
        print("\n✅ ¡Empleado agregado con éxito!")
        
    # ---------------------------------------------------------
    # OPCIÓN 2: BUSCAR EMPLEADO
    # ---------------------------------------------------------
    elif opcion == "2":
        print("\n--- BUSCAR EMPLEADO ---")
        busqueda = input("Ingresa el Nombre o ID del empleado a buscar: ")
        encontrado = False
        
        # Revisamos cada empleado que está en la lista
        for empleado in lista_empleados:
            # Si el texto buscado coincide con el ID o con el Nombre...
            if busqueda == empleado["id"] or busqueda.lower() in empleado["nombre"].lower():
                print("\n📌 Empleado Encontrado:")
                print("ID:", empleado["id"])
                print("Nombre Completo:", empleado["nombre"], empleado["apellido"])
                print("Cargo:", empleado["cargo"])
                print("Departamento:", empleado["departamento"])
                print("Salario: $", empleado["salario"])
                print("Fecha Contratación:", empleado["fecha"])
                print("-" * 30)
                encontrado = True
                
        if encontrado == False:
            print("❌ No se encontró ningún empleado con ese criterio.")
            
    # ---------------------------------------------------------
    # OPCIÓN 3: ACTUALIZAR EMPLEADO
    # ---------------------------------------------------------
    elif opcion == "3":
        print("\n--- ACTUALIZAR INFORMACIÓN ---")
        id_buscar = input("Ingresa el ID del empleado que quieres modificar: ")
        encontrado = False
        
        for empleado in lista_empleados:
            if empleado["id"] == id_buscar:
                encontrado = True
                print(f"\nModificando a: {empleado['nombre']} {empleado['apellido']}\n")
                
                # Preguntamos por los datos nuevos. Si se deja en blanco, se queda el dato anterior.
                nuevo_cargo = input(f"Nuevo Cargo (Actual: {empleado['cargo']}): ")
                if nuevo_cargo != "":
                    empleado["cargo"] = nuevo_cargo
                    
                nuevo_dep = input(f"Nuevo Departamento (Actual: {empleado['departamento']}): ")
                if nuevo_dep != "":
                    empleado["departamento"] = nuevo_dep
                    
                nuevo_salario = input(f"Nuevo Salario (Actual: {empleado['salario']}): ")
                if nuevo_salario != "":
                    empleado["salario"] = nuevo_salario
                    
                print("\n✅ Información actualizada correctamente.")
                break # Rompe el bucle for porque ya encontramos al empleado
                
        if encontrado == False:
            print("❌ No se encontró ningún empleado con ese ID.")

    # ---------------------------------------------------------
    # OPCIÓN 4: ELIMINAR EMPLEADO
    # ---------------------------------------------------------
    elif opcion == "4":
        print("\n--- ELIMINAR EMPLEADO ---")
        id_borrar = input("Ingresa el ID del empleado que deseas borrar: ")
        encontrado = False
        
        for empleado in lista_empleados:
            if empleado["id"] == id_borrar:
                # Quitamos al empleado de la lista usando .remove()
                lista_empleados.remove(empleado)
                print(f"🗑️ El empleado con ID {id_borrar} fue eliminado.")
                encontrado = True
                break
                
        if encontrado == False:
            print("❌ No se encontró ningún empleado con ese ID.")

    # ---------------------------------------------------------
    # OPCIÓN 5: SALIR
    # ---------------------------------------------------------
    elif opcion == "5":
        print("👋 Gracias por usar el sistema. ¡Adiós!")
        ejecutando = False # Esto hace que el bucle while termine
        
    # Si el usuario escribe una opción que no es del 1 al 5
    else:
        print("⚠️ Opción inválida. Por favor, elige un número del 1 al 5.")