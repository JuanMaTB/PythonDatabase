from Registro import *

# Listas para almacenar los objetos
alumnos = GestorDatos.cargar_datos("alumnos.json")
profesores = GestorDatos.cargar_datos("profesores.json")
clases = GestorDatos.cargar_datos("clases.json")
facturas = GestorDatos.cargar_datos("facturas.json")
anticipos = GestorDatos.cargar_datos("anticipos.json")


def registrar_alumno():
    """Registra un nuevo alumno y lo guarda en JSON."""
    print("\n--- Registrar Alumno ---")
    num_registro = input("Número de registro (ej: 2025/001): ")
    nombre = input("Nombre: ")
    primer_apellido = input("Primer apellido: ")
    segundo_apellido = input("Segundo apellido: ")
    dni = input("DNI (ej: 12345678A): ")
    fecha_nacimiento = input("Fecha de nacimiento (DD-MM-AAAA): ")
    fecha_registro = input("Fecha de registro (DD-MM-AAAA): ")
    permiso_opta = input("Permiso al que opta (A, B, C, etc.): ")
    domicilio = input("Domicilio: ")
    municipio = input("Municipio: ")
    provincia = input("Provincia: ")
    telefono1 = input("Teléfono 1: ")
    telefono2 = input("Teléfono 2 (opcional): ") or None
    correo = input("Correo electrónico: ")
    num_clases = int(input("Número de clases: "))
    profesor = input("Nombre del profesor: ")

    nuevo_alumno = Alumno(num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento,
                          fecha_registro, permiso_opta, domicilio, municipio, provincia, telefono1, telefono2, correo,
                          num_clases, profesor)

    alumnos.append(nuevo_alumno)
    GestorDatos.guardar_datos("alumnos.json", alumnos)
    print("\n✅ Alumno registrado correctamente.\n")


def registrar_profesor():
    """Registra un nuevo profesor y lo guarda en JSON."""
    print("\n--- Registrar Profesor ---")
    nombre = input("Nombre: ")
    primer_apellido = input("Primer apellido: ")
    segundo_apellido = input("Segundo apellido: ")
    vehiculo = input("Matrícula del vehículo: ")
    tipo_vehiculo = input("Tipo de vehículo: ")
    itv = input("Fecha de vencimiento de la ITV (DD-MM-AAAA): ")

    nuevo_profesor = Profesor(nombre, primer_apellido, segundo_apellido, vehiculo, tipo_vehiculo, itv)

    profesores.append(nuevo_profesor)
    GestorDatos.guardar_datos("profesores.json", profesores)
    print("\n✅ Profesor registrado correctamente.\n")


def registrar_clase():
    """Registra una nueva clase y la guarda en JSON."""
    print("\n--- Registrar Clase ---")
    alumno = input("DNI del alumno: ")
    profesor = input("DNI del profesor: ")
    matricula_vehiculo = input("Matrícula del vehículo usado: ")
    fecha_hora = input("Fecha y hora de la clase (DD-MM-AAAA HH:MM): ")

    nueva_clase = Clase(alumno, profesor, matricula_vehiculo, fecha_hora)
    clases.append(nueva_clase)
    GestorDatos.guardar_datos("clases.json", clases)
    print("\n✅ Clase registrada correctamente.\n")


def registrar_anticipo():
    """Registra un anticipo de pago y lo guarda en JSON."""
    print("\n--- Registrar Anticipo ---")
    alumno = input("DNI del alumno: ")
    fecha = input("Fecha del anticipo (DD-MM-AAAA): ")
    concepto = input("Concepto del anticipo: ")
    cantidad = float(input("Cantidad (€): "))

    nuevo_anticipo = Anticipo(alumno, fecha, concepto, cantidad)
    anticipos.append(nuevo_anticipo)
    GestorDatos.guardar_datos("anticipos.json", anticipos)
    print("\n✅ Anticipo registrado correctamente.\n")


def generar_factura():
    """crea una factura para un alumno."""
    print("\n--- Generar Factura ---")
    alumno = input("DNI del alumno: ")
    precio_matricula = float(input("Precio de la matrícula (€): "))
    num_clases_incluidas = int(input("Número de clases incluidas: "))
    num_clases_dadas = int(input("Número total de clases dadas: "))
    precio_clase = float(input("Precio por clase adicional (€): "))
    num_examenes = int(input("Número de exámenes realizados: "))
    precio_examen = float(input("Precio del examen (€): "))
    num_renovaciones = int(input("Número de renovaciones: "))
    precio_renovacion = float(input("Precio de renovación (€): "))
    anticipos_total = float(input("Total de anticipos (€): "))

    nueva_factura = Factura(alumno, precio_matricula, num_clases_incluidas, num_clases_dadas,
                            precio_clase, num_examenes, precio_examen, num_renovaciones, precio_renovacion, anticipos_total)

    facturas.append(nueva_factura)
    GestorDatos.guardar_datos("facturas.json", facturas)

    print("\n✅ Factura generada correctamente.\n")
    nueva_factura.generar_factura()


def mostrar_menu():
    """muestra el menú interactivo y gestiona la eleccion del usuario"""
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar Alumno")
        print("2. Registrar Profesor")
        print("3. Registrar Clase")
        print("4. Registrar Anticipo")
        print("5. Generar Factura")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            registrar_profesor()
        elif opcion == "3":
            registrar_clase()
        elif opcion == "4":
            registrar_anticipo()
        elif opcion == "5":
            generar_factura()
        elif opcion == "6":
            print("Saliendo del programa... 🚪")
            break
        else:
            print("⚠⚠⚠⚠⚠⚠ Opcion no valida. Intente nuevamente ⚠⚠⚠⚠⚠")
