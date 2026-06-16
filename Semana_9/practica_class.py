# CAMILLAS
class Camilla:
    def __init__(self, disponibilidad, sistema, movilidad):
        self.disponibilidad = disponibilidad
        self.sistema = sistema
        self.movilidad = movilidad

    def __str__(self):
        return f"\nCamillas:\nDisponibilidad: {self.disponibilidad}\nSistema: {self.sistema}\nMovilidad: {self.movilidad}"

camilla1 = Camilla(2, "Electrica", "Ruedas")
print(camilla1)


# EQUIPO
class Equipo:
    def __init__(self, tipo, nombre, bateria):
        self.tipo = tipo
        self.nombre = nombre
        self.bateria = bateria

    def encender(self):
        return "Equipo encendiendo..."

    def apagar(self):
        return "Equipo apagando..."

    def __str__(self):
        return f"\nEquipo:\nTipo: {self.tipo}\nNombre: {self.nombre}\nBateria: {self.bateria}"

monitor = Equipo("Electronico", "Monitor", True)
print(monitor)
print(monitor.encender())


# AMBULANCIA
class Ambulancia:
    def __init__(self, pasajeros, placa):
        self.nombre = "Ambulancia"
        self.pasajeros = pasajeros
        self.placa = placa
        self.accesorios = []

    def agregar_accesorio(self, accesorio):
        self.accesorios.append(accesorio)

    def __str__(self):
        return f"\nVehiculo:\nTipo: {self.nombre}\nPasajeros: {self.pasajeros}\nPlaca: {self.placa}\nAccesorios: {self.accesorios}"

ambulancia1 = Ambulancia(4, "GVO-2765")
ambulancia2 = Ambulancia(6, "ABC-1234")

ambulancia1.agregar_accesorio(monitor)
print(ambulancia1)
print(ambulancia2)


# HABITACIONES
class Habitacion:
    def __init__(self, capacidad, climatizacion, visitas):
        self.capacidad = capacidad
        self.climatizacion = climatizacion
        self.visitas = visitas

    def __str__(self):
        return f"\nHabitaciones:\nCapacidad: {self.capacidad}\nClimatizacion: {self.climatizacion}\nVisitas: {self.visitas}"

habitacion1 = Habitacion(10, True, True)
print(habitacion1)


# MEDICOS
class Medico:
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad

    def atender(self):
        return f"{self.nombre} está atendiendo un paciente."

    def __str__(self):
        return f"\nMedicos:\nNombre: {self.nombre}\nEdad: {self.edad}\nEspecialidad: {self.especialidad}"

medico1 = Medico("Paul", 35, "Medicina General")
medico2 = Medico("Luisa", 40, "Psiquiatria")
print(medico1)
print(medico2)
print(medico1.atender())


# AREAS
class Area:
    def __init__(self, nombre, disponibilidad):
        self.nombre = nombre
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"\nAreas:\nNombre: {self.nombre}\nDisponibilidad: {self.disponibilidad}"


area1 = Area("Sala de Espera", True)
area2 = Area("Pediatria", False)
print(area1)
print(area2)


# PACIENTES
class Paciente:
    def __init__(self, nombre, dni, direccion):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        self.historia_clinica = []

    def agregar_historial(self, dato):
        self.historia_clinica.append(dato)

    def __str__(self):
        return f"\nPacientes:\nNombre: {self.nombre}\nDNI: {self.dni}\nDireccion: {self.direccion}\nHistoria Clinica: {self.historia_clinica}"

paciente1 = Paciente("Luis", "097772656730", "Av. Quito")
paciente2 = Paciente("Carmen", "0977726112", "Av. Salmos")

paciente1.agregar_historial("Control General")
print(paciente1)
print(paciente2)


# SILLAS
class Silla:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"\nSillas:\nTipo: {self.tipo}"

silla1 = Silla("Metal")
print(silla1)


# MEDICINAS
class Medicina:
    def __init__(self, nombre, marca, disponibilidad):
        self.nombre = nombre
        self.marca = marca
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"\nMedicinas:\nNombre: {self.nombre}\nMarca: {self.marca}\nDisponibilidad: {self.disponibilidad}"

medicina1 = Medicina("Paracetamol", "Bloxin", True)
print(medicina1)


# ENFERMEDADES
class Enfermedad:
    def __init__(self, nombre, codigo, tipo):
        self.nombre = nombre
        self.codigo = codigo
        self.tipo = tipo

    def __str__(self):
        return f"\nEnfermedades:\nNombre: {self.nombre}\nCodigo: {self.codigo}\nTipo: {self.tipo}"

enfermedad1 = Enfermedad("Viruela", "CGI-009", "Viral")
print(enfermedad1)


# HISTORIAL CLINICO
class HistorialClinico:
    def __init__(self, fecha):
        self.fecha = fecha
        self.pacientes = []
        self.enfermedades = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_enfermedad(self, enfermedad):
        self.enfermedades.append(enfermedad)

    def __str__(self):
        return f"\nHistorial Clinico:\nFecha: {self.fecha}\nPacientes: {self.pacientes}\nEnfermedades: {self.enfermedades}"

historial1 = HistorialClinico("05/05/2026")

historial1.agregar_paciente(paciente1.nombre)
historial1.agregar_enfermedad(enfermedad1.nombre)
print(historial1)