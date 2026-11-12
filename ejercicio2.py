print("¡Bienvenido al sistema de gestión de equipos del Laboratorio Central de Investigación!")

equiposDisponibles = 25
historialUsos = 0
capacidadMaxima = 25
sistemaActivo = True

while sistemaActivo:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Equipos disponibles.")
    print("2.- Asignar equipo.")
    print("3.- Liberar equipo.")
    print("4.- Historial de usos.")
    print("5.- Salir.")
    
    opcionElegida = 0
    
    menuValido = False
    while not menuValido:
        try:
            opcionElegida = int(input("Seleccione una opción: "))
            menuValido = True
        except:
            print("¡Opción inválida! Por favor, ingrese un número entero correspondiente al menú.")

    match opcionElegida:
        case 1:
            print(f"Cantidad actual de equipos disponibles: {equiposDisponibles}")
        case 2:
            cantidadAsignar = 0
            asignacionValida = False
            while not asignacionValida:
                try:
                    cantidadAsignar = int(input("Ingrese la cantidad de equipos a asignar: "))
                    if cantidadAsignar <= 0:
                        print("La cantidad a asignar no puede ser menor o igual a 0.")
                    elif cantidadAsignar > equiposDisponibles:
                        print(f"No hay suficientes equipos disponibles. Disponibles actuales: {equiposDisponibles}")
                    else:
                        asignacionValida = True
                except:
                    print("¡Error! Ingrese un número entero válido.")
            
            equiposDisponibles -= cantidadAsignar
            historialUsos += cantidadAsignar
            print("¡Equipos asignados exitosamente!")
        case 3:
            cantidadLiberar = 0
            liberacionValida = False
            while not liberacionValida:
                try:
                    cantidadLiberar = int(input("Ingrese la cantidad de equipos a liberar: "))
                    if cantidadLiberar <= 0:
                        print("La cantidad a liberar debe ser mayor a 0.")
                    elif (equiposDisponibles + cantidadLiberar) > capacidadMaxima:
                        print(f"Error: Supera la capacidad máxima del laboratorio ({capacidadMaxima} equipos).")
                    else:
                        liberacionValida = True
                except:
                    print("¡Error! Ingrese un número entero válido.")
            
            equiposDisponibles += cantidadLiberar
            historialUsos -= cantidadLiberar
            print("¡Equipos liberados exitosamente!")
        case 4:
            print(f"Cantidad total de equipos asignados durante la sesión: {historialUsos}")
        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            sistemaActivo = False
        case _:
            print("Opción no válida. Por favor, elija un número entre 1 y 5.")