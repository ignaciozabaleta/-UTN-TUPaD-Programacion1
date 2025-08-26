'''1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
'''
edad = int(input("Ingrese su edad"))
if edad >= 18:
    print("Es mayor de edad")

    
'''2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
'''
nota = int(input("Ingrese su nota"))
if nota >= 6:
    print("Aprobado")
elif nota < 6:
    print("Desaprobado")


'''3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
'''    
num = int(input("Ingrese su num"))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


'''4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''    
edad = int(input("Ingrese su edad"))
if edad < 12:
    print("Usted es un/a niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es adolecente")
elif edad >= 18 and edad < 30:
    print("Usted es un/a adulto/a joven")
else:
    print("Usted es un/a adulto/a")
    
    
'''5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
'''
contraseña = str(input("Ingrese su una contraseña"))
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


'''6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
'''
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(numeros_aleatorios)
from statistics import mode, median, mean
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif moda == mediana == media:
    print("No hay sesgo")


'''7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
'''
frase = str(input("Ingrese una frase o palabra"))
vocales = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")
if frase.endswith(vocales):
    print(frase,"!",sep='')
else:
    print(frase)


'''8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''
nombre = str(input("Ingrese su nombre"))
opcion = int(input("Ingrese 1 si desea su nombre en mayúsculas, 2 si desea su nombre en minúsculas y 3 si desea la primera letra en mayúsucula"))
may = nombre.upper()
min = nombre.lower()
primeraletra = nombre.title()
if opcion == 1:
    print(may)
elif opcion == 2:
    print(min)
elif opcion == 3:
    print(primeraletra)


'''9)Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
'''
magnitud = float(input("Ingrese la magnitud del terremoto"))
if magnitud < 3:
    print("Muy leve, imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("Leve, ligeramnte perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado, sentido por personas, pero generalmente no causa daños")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte, puede causar daños en estructuras débiles")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte, puede causar daños significativos")
elif magnitud >= 7:
    print("Extremo, puede causar graves daños a gran escala")


'''7) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
''' 
hemisferio = str(input("En que hemisferio se encuentra?(N/S)"))
hemisferio = hemisferio.lower()              
mes = str(input("En que mes del año es?"))
mes = mes.lower()            
dia = int(input("Que día es?"))                          
if mes == "enero" or mes == "febrero":
    if hemisferio == "n":
        print("Invierno")
    elif hemisferio == "s":
        print("Verano")
elif mes == "diciembre":
    if dia >= 21:
        if hemisferio == "n":
            print("Invierno")
        elif hemisferio == "s":
            print("Verano")
    elif dia < 21:
        if hemisferio == "n":
            print("Otonio")
        elif hemisferio == "s":
            print("Primavera")
elif mes == "abril" or mes == "mayo":
    if hemisferio == "n":
        print("Primavera")
    elif hemisferio == "s":
        print("Otoño")
elif mes == "marzo":
    if dia >= 21:
        if hemisferio == "n":
            print("Primavera")
        elif hemisferio == "s":
            print("Otoño")
    elif dia < 21:
        if hemisferio == "n":
            print("Invierno")
        elif hemisferio == "s":
            print("Verano")
elif mes == "julio" or mes == "agosto":
    if hemisferio == "n":
        print("Verano")
    elif hemisferio == "s":
        print("Invierno")
elif mes == "junio":
    if dia >= 21:
        if hemisferio == "n":
            print("Verano")
        elif hemisferio == "s":
            print("Invierno")
    elif dia < 21:
        if hemisferio == "n":
            print("Primavera")
        elif hemisferio == "s":
            print("Otoño")        
elif mes == "octubre" or mes == "noviembre":
    if hemisferio == "n":
        print("Otoño")
    elif hemisferio == "s":
        print("Primavera")
elif mes == "septiembre":
    if dia >= 21:
        if hemisferio == "n":
            print("Otoño")
        elif hemisferio == "s":
            print("Primavera")
    elif dia < 21:
        if hemisferio == "n":
            print("Verano")
        elif hemisferio == "s":
            print("Invierno")    
                

        