# POO - Proceso de administracion:
# Representacion de ambientes
# Laboratorio:
computadora={'marca':'thinkcentre','anio':2020,'pulgadas':15.6,'periferico':['mouse''teclado']}
pizarra={'forma':'rectangular','color':'blanca','dimensiones':{'largo':100,'alto':60}}
tv={'marca':'samsung','pulgadas':55,'color':'negro'}

# Habitacion:
cama ={'plaza': 2, 'material':'madera','color':'negro'}
colchon={'palza':2,'marca':'chaide',' color':'blanco'}
ropero ={'material': 'madera', 'color': 'negro','dimensiones':[180,150]}

#desarrollar un software
#administrar banco:
bobeda={'dimesiones':[800,800],'material':'titaniu'}
monitor={'marca':'thinkcentre','anio':2020,'pulgadas':15.6,'periferico':['mouse''teclado']}
cuentas={'credito':1000,'hipotecas':'bien inmueble','debito':0}
carro={'modelo':'blindado','diseño':'4x4','llanta':'antideslizante'}
seguridad={'raza':'mestizo','altura':180,'implento':['arma','tolete']}

# APP Delivery:
local1={'nombre': 'kfc','direccion':'Av. Luis lopes','tiempo_espera':15,'tipo':'fast_food'}
local2={'nombre': 'macdonals','direccion':'Av. Luis lopes','tiempo_espera':15,'tipo':'fast_food'}
cliente={'dni':'0989876788','direccion':'cdl universitaria','numero':'0988542178','nombre':'pablo'}
colaborador={'nacionalidad':'venezuela','tipo_vehiculo':'moto','nombre':'luis'}

metodo_pago1={'tipo':'efectivo','descripcion':'moneda_local'}
metodo_pago2 = {'tipo':'transferencia','descripcion':'Pago por medio de apps bancarias'}
entidad_bancaria1={'nombre':'guayaquil'}
entidad_bancaria2={'nombre':'pichincha'}

# CLASES:
# Definir clases:
class Local:
    def __init__(self,nombre,direccion,tiempo_espera,tipo):
        self.nombre=nombre
        self.direccion=direccion
        self.tiempo_espera=tiempo_espera
        self.tipo=tipo

    def __str__(self):
        return f'nombre:{self.nombre},direccion:{self.direccion}'
# Instanciar la clase:
local3=Local('rukito','aventura plaza',15,'asado')
print(local3)
class Colaborador:
    def __init__(self, nacionalidad, tipo_vehiculo, nombre):
        self.nacionalidad = nacionalidad
        self.tipo_vehiculo = tipo_vehiculo
        self.nombre = nombre
# Instanciar la clase:
colaborador3=Colaborador('ecuador','carro','pablito')
















