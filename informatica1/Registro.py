""" Registro va a ser la base para almacenar
    toda la informacion de los alumnos
"""
#Aqui definimos la clase Registro, que sera como el molde de cada objeto
class Registro:

     """definimos el metodo que usaremos, __init__ para crear los objetos siguiendo el molde (la class Registro)
        si no inclutesemos self no se guardaria en memoria el objeto"""
     def __init__(self, num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta):
        # ahora inicializamos los atributos con los valores que hemos definido para crear un objeto de Registro
        self.num_registro = num_registro
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_registro = fecha_registro
        self.permiso_opta = permiso_opta


     def mostrar_datos(self):
        # formateamos con (f"Enunciado: {self.atributo}") para que sea legible
        print(f"Registro: {self.num_registro}")
        print(f"Nombre completo: {self.nombre} {self.primer_apellido} {self.segundo_apellido}")
        print(f"DNI: {self.dni}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de registro: {self.fecha_registro}")
        print(f"Permiso al que opta: {self.permiso_opta}")

class Alumno(Registro):
     def __init__(self, num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta,
                    domicilio, municipio, provincia, telefono1, telefono2=None, correo="", num_clases=0, profesor=""):
        # hay que iniciar los atributos de la clase padre (Registro)
        super().__init__(num_registro, nombre, primer_apellido, segundo_apellido, dni, fecha_nacimiento, fecha_registro, permiso_opta)
        # ahora inicializamos los atributos con los valores que hemos definido para crear un objeto de Alumno
        self.domicilio = domicilio
        self.municipio = municipio
        self.provincia = provincia
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.correo = correo
        self.num_clases = num_clases
        self.profesor = profesor
        self.examenes_teoricos = []
        self.examenes_circulacion = []

        # ahora definimos el metodos para cambiar fechas de examenes y que impriman que el cambio se ha hecho
     def agregar_examen_teorico(self, fecha_hora):
         self.examenes_teoricos.append(fecha_hora)
         print(f"Examen teorico añadido: {fecha_hora}")
     def agregar_examen_circulacion(self, fecha_hora):
         self.examenes_circulacion.append(fecha_hora)
         print(f"Examen de circulacion añadido: {fecha_hora}")
     def agregar_clase(self, num):
         self.num_clases += num
         print(f"{num} clases añadidas. Total de clases ahora: {self.num_clases}")

        # usare el metodo de mostrar datos, el padre para añadir los datos que faltan
     def mostrar_datos(self):
        # metodo para mostrar toda la información del alumno
        super().mostrar_datos()
        # Añadimos los datos específicos de Alumno
        print(f"Domicilio: {self.domicilio}, {self.municipio}, {self.provincia}")
        print(f"Teléfonos: {self.telefono1}, {self.telefono2}")
        print(f"Correo: {self.correo}")
        print(f"Número de Clases: {self.num_clases}")
        print(f"Profesor: {self.profesor}")
        print(f"Exámenes Teóricos: {self.examenes_teoricos}")
        print(f"Exámenes Circulación: {self.examenes_circulacion}")

    # clase para gestionar la información de los profesores
class Profesor:

    def __init__(self, nombre, primer_apellido, segundo_apellido, vehiculo, tipo_vehiculo, itv):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.vehiculo = vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.itv = itv
        self.gastos_combustible = {}  # Diccionario: {fecha: costo}

    def registrar_gasto_combustible(self, fecha, costo):

        if fecha in self.gastos_combustible:
            self.gastos_combustible[fecha] += costo
        else:
            self.gastos_combustible[fecha] = costo
        print(f"Gasto de combustible registrado: {fecha} - {costo:.2f}€")

    def mostrar_gastos_combustible(self):

        print("\n--- Gastos de Combustible ---")
        for fecha, costo in self.gastos_combustible.items():
            print(f"{fecha}: {costo:.2f}€")

    def mostrar_info_profesor(self):
        """Muestra la información completa del profesor y su vehículo."""
        print("\n--- Información del Profesor ---")
        print(f"Nombre completo: {self.nombre} {self.primer_apellido} {self.segundo_apellido}")
        print(f"Vehículo: {self.vehiculo} ({self.tipo_vehiculo})")
        print(f"ITV válida hasta: {self.itv}")

        # clase para gestionar las sesiones entre un alumno y un profesor
class Clase:

    def __init__(self, alumno: str , profesor: str, matricula_vehiculo: str, fecha_hora: str):
        self.alumno = alumno  # DNI del alumno ya que es un valor unico
        self.profesor = profesor  # DNI del profesor ya que es un valor unico
        self.matricula_vehiculo = matricula_vehiculo
        self.fecha_hora = fecha_hora


    def mostrar_info_clase(self):
        print("\n--- Información de la Clase ---")
        print(f"Alumno (DNI): {self.alumno}")
        print(f"Profesor (DNI): {self.profesor}")
        print(f"Vehículo utilizado: {self.matricula_vehiculo}")
        print(f"Fecha y hora de la clase: {self.fecha_hora}")

    # para gestionar los permisos en la autoescuela
class Permiso:

    def __init__(self,
                 tipo_permiso: str,
                 precio_matricula: float,
                 clases_incluidas: int,
                 precio_por_clase: float,
                 precio_examen: float,
                 precio_renovacion: float):
        self.tipo_permiso: str = tipo_permiso  # Tipo de licencia (ej. "A", "B")
        self.precio_matricula: float = precio_matricula  # Costo de la matrícula
        self.clases_incluidas: int = clases_incluidas  # Número de clases incluidas
        self.precio_por_clase: float = precio_por_clase  # Costo por clase adicional
        self.precio_examen: float = precio_examen  # Costo del examen
        self.precio_renovacion: float = precio_renovacion  # Costo de la renovación

    def mostrar_info_permiso(self):

        print("\n--- Información del Permiso ---")
        print(f"Tipo de Permiso: {self.tipo_permiso}")
        print(f"Precio de Matrícula: {self.precio_matricula:.2f}€")
        print(f"Clases Incluidas: {self.clases_incluidas}")
        print(f"Precio por Clase Adicional: {self.precio_por_clase:.2f}€")
        print(f"Precio del Examen: {self.precio_examen:.2f}€")
        print(f"Precio de Renovación: {self.precio_renovacion:.2f}€")


    # facturacion en la autoescuela
class Factura:

    def __init__(self, alumno, precio_matricula, num_clases_incluidas, num_clases_dadas, precio_clase, num_examenes, precio_examen, num_renovaciones, precio_renovacion, anticipos):
        self.alumno = alumno  # DNI del alumno
        self.precio_matricula = precio_matricula
        self.num_clases_incluidas = num_clases_incluidas
        self.num_clases_dadas = num_clases_dadas
        self.precio_clase = precio_clase
        self.num_examenes = num_examenes
        self.precio_examen = precio_examen
        self.num_renovaciones = num_renovaciones
        self.precio_renovacion = precio_renovacion
        self.anticipos = anticipos

    def calcular_total(self):
        # SIN IVA
        costo_clases_extra = max(0, self.num_clases_dadas - self.num_clases_incluidas) * self.precio_clase
        total = (self.precio_matricula + costo_clases_extra +
                 self.num_examenes * self.precio_examen +
                 self.num_renovaciones * self.precio_renovacion)
        return total

    def calcular_iva(self):
        #IVA
        return self.calcular_total() * 0.21

    def calcular_total_con_iva(self):
        # CON IVA
        return self.calcular_total() + self.calcular_iva()

    def calcular_saldo_pendiente(self):
        # Saldo despues de anticipos
        return max(0, self.calcular_total_con_iva() - self.anticipos)

    def generar_factura(self):
        # resumen de facturacion
        print("\n--- Factura ---")
        print(f"Alumno (DNI): {self.alumno}")
        print(f"Precio de Matrícula: {self.precio_matricula:.2f}€")
        print(f"Número de Clases Dadas: {self.num_clases_dadas}")
        print(f"Clases Incluidas en Matrícula: {self.num_clases_incluidas}")
        print(f"Precio por Clase Adicional: {self.precio_clase:.2f}€")
        print(f"Precio del Examen: {self.precio_examen:.2f}€")
        print(f"Número de Exámenes: {self.num_examenes}")
        print(f"Precio de Renovación: {self.precio_renovacion:.2f}€")
        print(f"Número de Renovaciones: {self.num_renovaciones}")
        print(f"Anticipos Realizados: {self.anticipos:.2f}€")
        print(f"Total sin IVA: {self.calcular_total():.2f}€")
        print(f"IVA (21%): {self.calcular_iva():.2f}€")
        print(f"Total con IVA: {self.calcular_total_con_iva():.2f}€")
        print(f"Saldo Pendiente: {self.calcular_saldo_pendiente():.2f}€")

    # registro de anticipos
class Anticipo:

    def __init__(self, alumno, fecha, concepto, cantidad):
        self.alumno = alumno  # DNI del alumno
        self.fecha = fecha
        self.concepto = concepto
        self.cantidad = cantidad

    # info completa del anticipo
    def mostrar_info_anticipo(self):

        print("\n--- Anticipo ---")
        print(f"Alumno (DNI): {self.alumno}")
        print(f"Fecha: {self.fecha}")
        print(f"Concepto: {self.concepto}")
        print(f"Cantidad: {self.cantidad:.2f}€")

"""//////////////////////  PERSISTENCIA DE DATOS EN JSON  ///////////////////////////"""

import json

class GestorDatos:
    """clase para gestionar la carga y guardado de datos."""

    @staticmethod
    def guardar_datos(archivo: str, datos: list) -> None:
        """guarda datos en un json"""
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([obj.__dict__ for obj in datos], f, indent=4, ensure_ascii=False)
        print(f"Datos guardados en {archivo}.")

    @staticmethod
    def cargar_datos(archivo: str):
        """carga datos desde un json"""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                # Verificar si el archivo está vacio pues si es asi el programa peta
                contenido = f.read().strip()
                if not contenido:
                    print(f"El archivo {archivo} está vacío. No se pudieron cargar datos.")
                    return []  # inicializamos datos vacíos y con esto ya salimos del paso. no es elegante. a mejorar
                # Intentar cargar datos JSON
                datos = json.loads(contenido)
                print(f"Datos cargados desde {archivo}.")
                return datos
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado. Creando con datos vacíos...")
            GestorDatos.guardar_datos(archivo, [])
            return []
        except json.JSONDecodeError:
            print(f"El archivo {archivo} está corrupto o no se puede leer como JSON.")
            return []  # Inicializamos datos vacíos




