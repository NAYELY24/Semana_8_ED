#POO
#Clases Identicas:
class asientoCine:
    def __init__(self):
        # Son atributos estaticos porque lo tendran todos los objetos
        self.color = "rojo"
        self.marca= "Figueras"

    #Para añadir metodos: Funcionalidades del objeto
    def reclinar(self):
        return f"Asiento reclinable"

    def enderezar(self):
        return f"Asiento enderezable"

    def __str__(self):
        return f"Color: {self.color}, Marca: {self.marca}"

#Iguales=silla1 y silla2
silla1=asientoCine()
print(silla1)

silla2=asientoCine()
print(silla2)

#Clases Parecidas:
class celulares:
    def __init__(self, pxcamara, mah):
        # Es un atributo estatico porque lo tendran todos los objetos
        # Si existe microfono (True)
        self.microfono=True
        #Atributo dinamico porque ciertos objetos poseen dichas caracteristicas
        self.pxcamara= pxcamara
        self.mah= mah

    # Para añadir metodos: Funcionalidades del objeto
    def encender(self):
            return f"Celular encendiendo..."

    def apagar(self):
            return f"Celular Apagando..."

    def __str__(self):
        return f"\n Microfono: {self.microfono}\n PxCamara: {self.pxcamara}\n mAh: {self.mah}"

celular1=celulares(48, 5000)
print(celular1)
print(f" {celular1.apagar()}")

celular2=celulares(12,3000)
#Para llamar a dicha funcionalidad (Linea 37)
print(celular2)
print(f" {celular2.encender()}")

#Ambiente Hospital
class camillas:
    def __init__(self, disponibilidad, sistema, movilidad):
        self.disponibilidad=disponibilidad
        self.sistema=sistema
        self.movilidad=movilidad
    def __str__(self):
        return f"\nCamillas:\nDisponibilidad: {self.disponibilidad}\nSistema: {self.sistema}\nMovilidad: {self.movilidad}"
camilla1=camillas(2, "Electrica", "Ruedas")
print(camilla1)


class equipo:
    def __init__(self, tipo, nombre, bateria):
        self.tipo = tipo
        self.nombre = nombre
        self.bateria = bateria

    def encender(self):
        return f"Equipo encendiendo..."

    def apagar(self):
        return f"Equipo apagando..."

    def __repr__(self):
        return self.nombre

    def __str__(self):
        return f"{self.tipo} - {self.nombre} - {self.bateria}"

monitor = equipo("Electronico", "Monitor", True)
print(monitor)

class ambulancia:
    def __init__(self, pasajeros, placa):
        self.nombre = "Ambulancia"
        self.accesorios =[]
        self.pasajeros=pasajeros
        self.placa=placa

    def __str__(self):
        return f"\nVehiculos:\nTipo: {self.nombre}\nPasajeros: {self.pasajeros}\nPlaca: {self.placa}\nAccesorios: {self.accesorios}"


ambulancia1=ambulancia("Ambulancia", "GVO-2765")
ambulancia2=ambulancia("Ambulancia",  "GVO-2765")

ambulancia1.accesorios.append(monitor)
ambulancia2.accesorios.append(monitor)
print(ambulancia1)
print(ambulancia2)






#Apuntes:
#Clase: Modelo o Molde de un atributo
#__init__: Metodo constructor
#self: Programar dentro de la clase, una forma de representar las caracteristicas
#Programar sin self: Afuera de la clase
#__str__: Devuelve objetos de una clase instanciada

