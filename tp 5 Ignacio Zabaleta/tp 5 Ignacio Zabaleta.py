'''
1) Crear una lista con las notas de 10 estudiantes. 
• Mostrar la lista completa. 
• Calcular y mostrar el promedio. 
• Indicar la nota más alta y la más baja. 
'''
notas = [6, 7, 3, 10, 4, 3, 1, 7, 9, 4]
suma = 0
for i in notas:
    i = notas
print("Las notas son", i)

suma = 0
for i in notas:
    suma = suma + i

promedio = suma / 10
print("El promedio es", promedio)

alto = 0
for i in notas:
    if i > alto:
        alto = i
print("La nota mas alta es", alto)

bajo = 10
for i in notas:
    if i < bajo:
        bajo = i
print("La nota masbaja es", bajo)



'''
2) Pedir al usuario que cargue 5 productos en una lista. 
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
• Preguntar al usuario qué producto desea eliminar y actualizar la lista. 
'''
productos = []
for i in range(5):
    nombre_producto = input(f"Ingresa el producto")
    productos.append(nombre_producto)
    
productos_ordenados = sorted(productos)
print(productos_ordenados)

producto_para_eliminar = input("¿Qué producto le gustaria eliminar?")
if producto_para_eliminar in productos:
    productos.remove(producto_para_eliminar)

print("Los productos son:", productos)


'''
3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
• Crear una lista con los pares y otra con los impares. 
• Mostrar cuántos números tiene cada lista. 
'''
import random
numeros_aleatorios = []

for i in range(15):
    numero_aleatorio = random.randint(1, 100)
    numeros_aleatorios.append(numero_aleatorio)

numeros_pares = []
numeros_impares = []
cantidad_pares = 0
cantidad_impares = 0

for i in numeros_aleatorios:
    if i % 2 == 0:
        numeros_pares.append(i)
        cantidad_pares = cantidad_pares + 1
    else:
        numeros_impares.append(i)
        cantidad_impares = cantidad_impares + 1

print("Los numero aleatorios son:", numeros_aleatorios)
print("Los numeros pares son:", numeros_pares)
print("Los numeros impares son:", numeros_impares)
print("La cantidad de numeros pares que hay es:", cantidad_pares)
print("La cantidad de numeros impares que hay es:", cantidad_impares)
 

'''
4) Dada una lista con valores repetidos: 
• Crear una nueva lista sin elementos repetidos. 
• Mostrar el resultado. 
'''
lista_con_repetidos = [1, 2, 2, 3, 4]
lista_sin_repetidos = []

for i in lista_con_repetidos:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)

print("La lista sin valores repetidos es:", lista_sin_repetidos)


'''
5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
• Mostrar la lista final actualizada. 
'''
lista_estudiantes = ["Juan Gomez", "Ignacio Gonzalez", "Martin Benitez", "Lautaro Ramirez", "Luis Sosa", "Laura Baez", "Maria Vera", "Claudia Ayala"]
nombre_para_eliminar = input("¿Qué nombre le gustaria eliminar?")
if nombre_para_eliminar in lista_estudiantes:
    lista_estudiantes.remove(nombre_para_eliminar)

nombre_para_agregar = input("¿Qué nombre le gustaria agregar?")
lista_estudiantes.append(nombre_para_agregar)

print("La lista final es:", lista_estudiantes)


'''
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
último pasa a ser el primero). 
'''
numeros = [1, 2, 3, 4, 5, 6, 7]

ultimo_elemento = numeros[-1]
resto = numeros[:-1]

nueva_lista = [ultimo_elemento] + resto
print(nueva_lista)


'''
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
semana. 
• Calcular el promedio de las mínimas y el de las máximas. 
• Mostrar en qué día se registró la mayor amplitud térmica.
'''
dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

semana = [
    [7, 18],
    [9, 22],
    [8, 19],
    [10, 24],
    [6, 20],
    [5, 17],
    [7, 21],
]

suma_min = 0
suma_max = 0

for i in semana:
    suma_min = suma_min + i[0]
    suma_max = suma_max + i[1]

prom_min = suma_min / 7
prom_max = suma_max / 7

mayor_amp = -1
indice_mayor = -1

for i in range(7):
    min_dia = semana[i][0]
    max_dia = semana[i][1]
    amp = max_dia - min_dia
    if amp > mayor_amp:
        mayor_amp = amp
        indice_mayor = i 

print("[min:max]:", semana)
print("Promedio minimas:", round(prom_min, 2))
print("Promedio maximas:", round(prom_max, 2))
print("Mayor amplitud en", dias[indice_mayor], "con", mayor_amp)


'''
8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
• Mostrar el promedio de cada estudiante. 
• Mostrar el promedio de cada materia. 
'''
estudiantes = ["Juan", "Pablo", "Maria", "Diego", "Carla"]
materias = ["Historia", "Matematicas", "Literatura"]

notas = [
    [8, 7, 6],
    [5, 9, 8],
    [10, 6, 9],
    [7, 7, 7],
    [6, 8, 5],
]

print("Notas:")
for i in range(len(estudiantes)):
    print(" ", estudiantes[i] + ":", notas[i])

print(" ")
print("Promedio:")
for i in range(len(estudiantes)):
    suma = 0
    for j in range(3):
        suma = suma + notas[i][j]
    prom = suma / 3
    print(" ", estudiantes[i] + ":", round(prom, 2))

print(" ")
print("Promedio por materia:")
for j in range(len(materias)):
    suma = 0
    for i in range(5):
        suma = suma + notas[i][j]
    prom = suma / 5
    print(" ", materias[j] + ":", round(prom, 2))


'''
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
• Inicializarlo con guiones "-" representando casillas vacías. 
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
• Mostrar el tablero después de cada jugada. 
'''


'''
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
• Mostrar el total vendido por cada producto. 
• Mostrar el día con mayores ventas totales. 
• Indicar cuál fue el producto más vendido en la semana. 
'''
ventas = [
    [2, 5, 6, 1, 7, 5, 6],
    [6, 1, 8, 6, 5, 3, 7],
    [1, 6, 7, 4, 8, 8, 3],
    [6, 4, 8, 5, 4, 3, 3]
]

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

totales_productos = []


for i in range(4):
    total_producto = 0
    for j in range(7):
        total_producto = total_producto + ventas[i][j]
    totales_productos.append(total_producto)
    print(f"Producto {i+1}: {total_producto}")

mayor_ventas = 0
dia_mayor = 0
for j in range(7):
    total_dia = 0
    for i in range(4):
        total_dia = total_dia + ventas[i][j]
    print(f"Total del dia {j+1}: {total_dia}")
    if total_dia > mayor_ventas:
        mayor_ventas = total_dia
        dia_mayor = j
print(f"El dia con mayores ventas fue el {dia_mayor+1}, con {mayor_ventas} ventas")

maximo_producto = 0
indice_producto = 0

for i in range(4):
    if totales_productos[i] > maximo_producto:
        maximo_producto = totales_productos[i]
        indice_producto = i

print(f"El producto mas vendido es el {indice_producto+1}, con {maximo_producto} ventas en la semana")