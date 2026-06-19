class Avion:
    def __init__(self, capacidad, aerolinea, color):
        self.nombre = 'avion'
        self.ambiente = 'aereo'
        self.num_ruedas = 3
        self.capacidad = capacidad
        self.aerolinea = aerolinea
        self.color = color
    def __str__(self):
        return f'nombre: {self.nombre}, color: {self.color}.'

avion_1 = Avion(60, 'Avianca', 'Blanco')
print(avion_1)

class Helicoptero:
    def __init__(self, marca, capacidad):
        self.nombre = 'helicoptero'
        self.ambiente = 'aereo'
        self.marca = marca
        self.capacidad = capacidad

    def __str__(self):
        return f'nombre:{self.nombre}, marca:{self.marca}.'


# HERENCIA:
# # Clase Padre:
# class Aeronaves:
#     def __init__(self, nombre, capacidad):
#         self.ambiente = 'aereo'
#         self.nombre = nombre
#         self.capacidad = capacidad
#
# # Clases Hijos:
# class AvionHerencia(Aeronaves):
#    def __init__(self, nombre, capacidad, aerolinea, color):
#         super().__init__(nombre, capacidad)
#         self.num_ruedas = 3
#         self.aerolinea = aerolinea
#         self.color = color
#
#    def __str__(self):
#         return f'Nombre: {self.nombre}, Aerolinea: {self.aerolinea}, Ambiente: {self.ambiente}.'
#
# # Instanciar:
# avion_2 = AvionHerencia('avion', 200, 'Turkish', 'azul')
# print(avion_2)
#
#
# class HelicopteroHerencia(Aeronaves):
#     def __init__(self,nombre, marca, capacidad):
#         super().__init__(nombre, capacidad)
#         self.marca = marca
#
#     def __str__(self):
#         return f'Nombre: {self.nombre}, Marca: {self.marca}, Capacidad: {self.capacidad}.'
#
# # Instanciar:
# helicoptero_2 = HelicopteroHerencia('Helicoptero', 'Avianca', '5')
# print(helicoptero_2)


# POLIMORFISMO:
# Clase Padre:
class Aeronaves:
    def __init__(self, nombre, capacidad):
        self.ambiente = 'aereo'
        self.nombre = nombre
        self.capacidad = capacidad
    # Metodo encender:
    def encender(self):
        return f'encendiendo motor...'

# Clases Hijos:
class AvionHerencia(Aeronaves):
   def __init__(self, nombre, capacidad, aerolinea, color):
        super().__init__(nombre, capacidad)
        self.num_ruedas = 3
        self.aerolinea = aerolinea
        self.color = color

   # Metodo encender:
   def encender(self):
        return f'encendiendo motor del avion...'

   def __str__(self):
        return f'Nombre: {self.nombre}, Aerolinea: {self.aerolinea}, Ambiente: {self.ambiente}.'

# Instanciar:
avion_2 = AvionHerencia('avion', 200, 'Turkish', 'azul')
print(avion_2)
print(avion_2.encender())


class HelicopteroHerencia(Aeronaves):
    def __init__(self,nombre, marca, capacidad):
        super().__init__(nombre, capacidad)
        self.marca = marca

    def __str__(self):
        return f'Nombre: {self.nombre}, Marca: {self.marca}, Capacidad: {self.capacidad}.'

# Instanciar:
helicoptero_2 = HelicopteroHerencia('Helicoptero', 'Avianca', '5')
print(helicoptero_2)









