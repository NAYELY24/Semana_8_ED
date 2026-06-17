# Ambiente deuna papeleria
class cuaderno:
    def __init__(self,cant_hoja,marca, tamanio, tipo):
        self.cant_hoja = cant_hoja
        self.marca = marca
        self.tamanio = tamanio
        self.tipo = tipo

class cliente:
    def __init__(self,nombre,dni,direccion):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion

    def __srt__(self):
        print(self.nombre, self.dni, self.direccion

class proveedor:
    def __init__(self, nombre, dni, empresa):
        self.nombre = nombre
        self.dni = dni
        self.empresa = empresa

    def __srt__(self):
        print(self.nombre, self.dni, self.empresa)

# Herencia
# Herencia padre:
class persona:
    def __init__(self,nombre,dni):
        self.nombre = nombre
        self.dni = dni

# Herencia hijos:
class clienteherencia(persona):
    def __init__(self,nombre,dni,direccion):
        super().__init__(nombre,dni)
        self.direccion = direccion

cliente_1=clienteherencia('Luis', 0122244, 'Av. Quito')
print(cliente_1.nombre)


class proveedorHerencia(persona):
    def __init__(self, nombre, dni, empresa):
        super().__init__(nombre, dni)
        self.empresa = empresa


proveedor_1 = proveedorHerencia('Luis', 0122244, 'Mi Comisariato')
print(proveedor_1.nombre)









