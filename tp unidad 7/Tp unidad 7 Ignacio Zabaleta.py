'''
1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 
'''
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

'''
2)Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800 
'''

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

'''
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. 
'''
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

'''
4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. 
'''
agenda = {}

nombre1 = input("Ingrese un nombre")
num1 = input("Ingrese el numero")
nombre2 = input("Ingrese un nombre")
num2 = input("Ingrese el numero")
nombre3 = input("Ingrese un nombre")
num3 = input("Ingrese el numero")
nombre4 = input("Ingrese un nombre")
num4 = input("Ingrese el numero")
nombre5 = input("Ingrese un nombre")
num5 = input("Ingrese el numero")

agenda[nombre1] = num1
agenda[nombre2] = num2
agenda[nombre3] = num3
agenda[nombre4] = num4
agenda[nombre4] = num4

consutar_agenda = input("Ingrese un nombre agendado")

if consutar_agenda in agenda:
    print(f"El numero de {consutar_agenda} es: {agenda[consutar_agenda]}")
else:
    print("El nombre ingresado no está agendado")

'''
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. 
'''
frase = input("Ingrese una frase")

palabras_unicas = set(frase.split())
print("Las palabras unicas son:",palabras_unicas)

diccionario_palabra = {}

for palabra in frase:
    if palabra in diccionario_palabra:
          diccionario_palabra[palabra] += 1
    else:
        diccionario_palabra[palabra] = 1


print(diccionario_palabra)

'''
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. 
'''
diccionario_alumnos = {}


alumno1 = input("Ingrese el nombre del primer alumno")
nota1_alumno1 = int(input("Ingrese su primer nota"))
nota2_alumno1 = int(input("Ingrese su segunda nota"))
nota3_alumno1 = int(input("Ingrese su tercer nota"))

diccionario_alumnos[alumno1] = (nota1_alumno1, nota2_alumno1, nota3_alumno1)
promedio_alumno1 = (nota1_alumno1 + nota2_alumno1 + nota3_alumno1) / 3

alumno2 = input("Ingrese el nombre del segundo alumno")
nota1_alumno2 = int(input("Ingrese su primer nota"))
nota2_alumno2 = int(input("Ingrese su segunda nota"))
nota3_alumno2 = int(input("Ingrese su tercer nota"))

diccionario_alumnos[alumno2] = (nota1_alumno2, nota2_alumno2, nota3_alumno2)
promedio_alumno2 = (nota1_alumno2 + nota2_alumno2 + nota3_alumno2) / 3

alumno3 = input("Ingrese el nombre del tercer alumno")
nota1_alumno3 = int(input("Ingrese su primer nota"))
nota2_alumno3 = int(input("Ingrese su segunda nota"))
nota3_alumno3 = int(input("Ingrese su tercer nota"))

diccionario_alumnos[alumno3] = (nota1_alumno3, nota2_alumno3, nota3_alumno3)
promedio_alumno3 = (nota1_alumno3 + nota2_alumno3 + nota3_alumno3) / 3

print(diccionario_alumnos)

print(f"El promedio de {alumno1} es {promedio_alumno1}")
print(f"El promedio de {alumno2} es {promedio_alumno2}")
print(f"El promedio de {alumno3} es {promedio_alumno3}")

'''
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 
'''


'''
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe. 
'''


'''
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
'''
agenda = {('lunes', '09:00'): 'Reunión', ('lunes', '11:00'): 'Llamada', ('martes', '10:00'): 'Revisión de informes', ('miércoles', '14:00'): 'Presentación'}

def consultar_evento(dia, hora):
    evento = agenda.get((dia, hora))
    if evento:
        return f"En {dia} a las {hora} hay: {evento}"
    else:
        return f"No hay eventos programados en {dia} a las {hora}"

print(consultar_evento('lunes', '09:00'))
print(consultar_evento('martes', '12:00'))


'''
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. 
'''
original = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago' }
invertido = {original['Argentina'] : 'Argentina', original['Chile']:'Chile'}

print(invertido) 