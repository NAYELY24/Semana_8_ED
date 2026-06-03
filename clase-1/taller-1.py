# 1. Representa la edad de una persona:
# Version 1:
lista=[]
edad=int(input("Ingrese edad: "))
lista.append(edad)
# Version 2:
edad2=20
# Version 3:
edad3=int(input("Ingrese edad: "))

# 2. Almacenar los datos de un cliente
cliente={"nombre":"juan", "id": 0989. }

# 3. Interaccion con una persona, un carro y una mascota:
persona = {"nombre": "juan", "edad": 25}
carro = {'modelo': 'toyota', 'ani': 2000}
mascota = {'tipo': 'perro', 'raza': 'siberiano', 'color': 'cafe'}

persona1={'nombre': 'juan', 'edad':25, 'modelo': 'toyota', 'ani': 2000, 'tipo': 'perro', 'raza': 'siberiano', 'color': 'cafe'}
pertenencia_persona={'persona' : persona, 'carro': carro, 'mascota': mascota}
# 4. Presentar el color de la mascota de la persona:
print(pertenencia_persona['mascota']['color'])

# 5. Representar una relacion amorosa:
persona1={'sexo':'masculino','nombre':'pedro','edad':20}
persona2={'sexo':'femenino','nombre':'julia','edad':18}
persona3={'sexo':'masculino','nombre':'julio','edad':30}

relacion={'novio':persona1,'novia2':persona2}
poligamia={'novio':persona1,'novia2':persona2,'novio3':persona3}

# 6. Presenta los monmbres de la pareja:
print(f'{relacion['novio']['nombre']}, {relacion['novia2']['nombre']}')
# 7. Presenta cuantas personas forman parte de la relacion:
print(f' {len(poligamia)}')
print(len(relacion['novio'])+len(relacion['novia2']))

# 8. Presentar si es una relacion monogamica o poligamica:
if (len(relacion['novio'])>1 or len(relacion['novia2'])>1):
    print(f'relacion poligamica')
else:
    print(f'relacion monogamica')

