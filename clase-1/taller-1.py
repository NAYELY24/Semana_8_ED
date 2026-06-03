# # Representacion de la edad de una persona
# lista=[]
# edad=int(input("Ingrese edad: "))
# lista.append(edad)
#
# edad2=20
#
#
# edad3=int(input("Ingrese edad: "))
#
# # Asignar un identificador a una persona
#
# # Almacenar los datos de un cliente
# cliente={"nombre":"juan", "id": 0989. }
#
# interaccion con un carro:
# modelo=input("Ingrese modelo: ")
# ani=int(input("ingresar el año"))
# persona={"nombre":"juan","edad":25}
# carro = {'modelo':'toyota', 'ani':2000}
# perro={'raza':'siberiano','color':'cafe'}
#
# persona1={'nombre':'juan','edad':25, 'modelo':'toyota', 'ani':2000, perro:perro, carro:carro}
# pertenencia_persona={'persona' : persona, 'carro': carro, 'perro': perro}
# #Presentar el colo de la mascota de la persona
# print(pertenencia_persona['perro']['color'])

# Representar una relacion amorosa
persona1={'sexo':'masculino','nombre':'pedro','edad':20}
persona2={'sexo':'femenino','nombre':'julia','edad':18}
persona3={'sexo':'masculino','nombre':'julio','edad':30}
relacion={'novio':persona1,'novia2':persona2}
poligamia={'novio':persona1,'novia2':persona2,'novio3':persona3}
print(f'{relacion['novio']['nombre']}, {relacion['novia2']['nombre']}')
print(f'  {len(poligamia)}')

print(len(relacion['novio'])+len(relacion['novia2']))

if (len(relacion['novio'])>1 or len(relacion['novia2'])>1):
    print(f'relacion poligamica')
else:
    print(f'relacion monogamica')

