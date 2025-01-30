#voy a importar del archivo Registro la clase Registro

from Registro import *
from menu import mostrar_menu

# Crear el primer alumno
alumno1 = Alumno(
    num_registro="2025/001",
    nombre="Juan",
    primer_apellido="Pérez",
    segundo_apellido="López",
    dni="12345678A",
    fecha_nacimiento="15-03-1995",
    fecha_registro="20-01-2025",
    permiso_opta="B",
    domicilio="Calle Falsa 123",
    municipio="Madrid",
    provincia="Madrid",
    telefono1="600123456",
    correo="juan@example.com",
    num_clases=10,
    profesor="Luis Gómez"
)

# Crear el segundo alumno
alumno2 = Alumno(
    num_registro="2025/002",
    nombre="Ana",
    primer_apellido="Sánchez",
    segundo_apellido="Gómez",
    dni="98765432B",
    fecha_nacimiento="22-07-1993",
    fecha_registro="21-01-2025",
    permiso_opta="A",
    domicilio="Avenida Siempre Viva 742",
    municipio="Sevilla",
    provincia="Sevilla",
    telefono1="600654321",
    correo="ana@example.com",
    num_clases=5,
    profesor="María Martínez"
)

# Mostrar la información  inicial de ambos alumnos
print("Datos del primer alumno:")
alumno1.mostrar_datos()

print("\nDatos del segundo alumno:")
alumno2.mostrar_datos()

# Añadir exámenes teóricos
print("\n--- Añadiendo exámenes teóricos ---")
alumno1.agregar_examen_teorico("22-01-2025 10:00")
alumno1.agregar_examen_teorico("25-01-2025 12:00")

# Añadir exámenes de circulación
print("\n--- Añadiendo exámenes de circulación ---")
alumno1.agregar_examen_circulacion("30-01-2025 09:00")

# Sumar clases realizadas
print("\n--- Añadiendo clases realizadas ---")
alumno1.agregar_clase(5)

# Mostrar la información actualizada del alumno
print("\n--- Información actualizada del alumno ---")
alumno1.mostrar_datos()

# crear un profesor
profesor1 = Profesor(
    nombre="Luis",
    primer_apellido="Gómez",
    segundo_apellido="Martínez",
    vehiculo="1234-ABC",
    tipo_vehiculo="Coche",
    itv="31-12-2025"
)

# Mostrar información inicial del profesor
profesor1.mostrar_info_profesor()

# Registrar gastos de combustible
profesor1.registrar_gasto_combustible("01-02-2025", 50)
profesor1.registrar_gasto_combustible("15-02-2025", 30)

# Mostrar gastos de combustible
profesor1.mostrar_gastos_combustible()


# crear una clase entre un alumno y un profesor
clase1 = Clase(
    alumno="12345678A",  # DNI del alumno (Juan)
    profesor="98765432B",  # DNI del profesor (Luis)
    matricula_vehiculo="1234-ABC",
    fecha_hora="01-03-2025 10:00"
)

# Mostrar la información de la clase
clase1.mostrar_info_clase()


# Crear un permiso de tipo "B"
permiso_b = Permiso(
    tipo_permiso="B",
    precio_matricula=200,
    clases_incluidas=10,
    precio_por_clase=25,
    precio_examen=50,
    precio_renovacion=80
)

# Crear un permiso de tipo "A"
permiso_a = Permiso(
    tipo_permiso="A",
    precio_matricula=150,
    clases_incluidas=8,
    precio_por_clase=30,
    precio_examen=45,
    precio_renovacion=70
)

# Mostrar la información de ambos permisos
permiso_b.mostrar_info_permiso()
permiso_a.mostrar_info_permiso()

from Registro import Factura, Anticipo

# Crear una factura para un alumno
factura1 = Factura(
    alumno="12345678A",  # DNI del alumno
    precio_matricula=200,
    num_clases_incluidas=10,
    num_clases_dadas=15,
    precio_clase=25,
    num_examenes=2,
    precio_examen=50,
    num_renovaciones=1,
    precio_renovacion=80,
    anticipos=150
)

# Generar la factura
factura1.generar_factura()

# Crear un anticipo
anticipo1 = Anticipo(
    alumno="12345678A",  # DNI del alumno
    fecha="10-01-2025",
    concepto="Pago inicial",
    cantidad=150
)

# Mostrar la información del anticipo
anticipo1.mostrar_info_anticipo()

# Guardar alumnos en un archivo json
GestorDatos.guardar_datos("alumnos.json", [alumno1, alumno2])

# Cargar alumnos desde json
alumnos_cargados = GestorDatos.cargar_datos("alumnos.json")
print(alumnos_cargados)

# Cargar menu
if __name__ == "__main__":
    mostrar_menu()




