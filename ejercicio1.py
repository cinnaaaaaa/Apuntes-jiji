print("--- Bienvenido al Instituto de Investigación Avanzada ---")

cantidadCientificos = 0
totalPrincipales = 0
totalAsistentes = 0

while cantidadCientificos <= 0:
    try:
        cantidadCientificos = int(input("¿Cuántos científicos desea ingresar?: "))
        if cantidadCientificos <= 0:
            print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")
    except:
        print("¡Dato de investigación inválido! Ingresa un entero positivo para continuar el registro.")

for cientificoActual in range(cantidadCientificos):
    print(f"\n--- Registro del científico {cientificoActual + 1} ---")
    
    
    idValido = False
    idCientifico = ""
    while not idValido:
        idCientifico = input("Ingrese el ID del científico (mínimo 12 caracteres, sin espacios): ")
        if len(idCientifico) >= 12 and " " not in idCientifico:
            idValido = True
        else:
            print("¡Error de registro! El ID debe tener al menos 12 caracteres y no debe incluir espacios.")

    
    numeroPublicaciones = -1
    while numeroPublicaciones < 0:
        try:
            numeroPublicaciones = int(input("Ingrese el número de publicaciones: "))
            if numeroPublicaciones < 0:
                print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")
        except:
            print("¡Error de registro! Ingresa un número entero positivo para el número de publicaciones.")


    if numeroPublicaciones > 12:
        totalPrincipales += 1
    else:
        totalAsistentes += 1

print(f"\n¡El instituto cuenta con {totalPrincipales} Investigadores Principales y {totalAsistentes} Investigadores Asistentes! ¡Ciencia en marcha!")