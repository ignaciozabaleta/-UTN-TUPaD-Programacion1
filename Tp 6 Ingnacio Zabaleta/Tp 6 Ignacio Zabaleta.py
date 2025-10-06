'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
volver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


nombre = input("Ingrese su nombre")

saludar_usuario(nombre)


'''
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores in
gresados.
'''
def Informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")


nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = input("I=ngrese su edad")
residencia = input("Ingrese su lugar de residencia")

Informacion_personal(nombre, apellido, edad, residencia)


'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
dio como parámetro y devuelva el área del círculo. calcular_peri
metro_circulo(radio) que reciba el radio como parámetro y devuel
va el perímetro del círculo. Solicitar el radio al usuario y llamar am
bas funciones para mostrar los resultados.
'''
from math import pi, pow

def calcular_area_circulo(radio):
    area = pi * pow(radio,2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2* pi *radio
    return perimetro

radio_usuario = (float(input("Ingrese el radio del circulo: ")))

area = calcular_area_circulo(radio_usuario)
perimetro =calcular_perimetro_circulo(radio_usuario)

print(f"El area del circulo es de {area}")
print(f"El perimetro del circulo es de {perimetro}")


'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función.
'''
from datetime import timedelta

def segundos_a_horas(segundos):
    horas = timedelta(seconds=segundos)
    return horas

segundos = int(input("Ingrese la cantidad de segundos: "))
print(segundos_a_horas(segundos))


'''
6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la fun
ción.
'''
def tabla_multiplicar(numero):
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

numero_usuario = int(input("Ingrese un numero para hacer su tabla de multiplicar: "))
tabla_multiplicar(numero_usuario)


'''
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara.
'''

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
   
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print(f"Suma: {operaciones_basicas(num1, num2)[0]}")
print(f"Resta: {operaciones_basicas(num1, num2)[1]}")
print(f"Multiplicación: {operaciones_basicas(num1, num2)[2]}")
print(f"División: {operaciones_basicas(num1, num2)[3]}")


'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
ción para mostrar el resultado con dos decimales.
'''
def calcular_imc(peso, altura):
    imc = peso / (peso * altura)
    round_imc = round(imc, 2)
    return round_imc
   
peso_usuario = int(input("Ingrese su peso en kilos: "))
altura_usuario = int(input("Ingrese su altura en metros: "))

print(f"Su IMC es {calcular_imc(peso_usuario, altura_usuario)}.")


'''
9.  Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
'''
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (5/9) + 32
    return fahrenheit
   
celsius_usuario = float(input("Ingrese la temperatura en celsius: "))

print(f"La temperatura es de {celsius_a_fahrenheit(celsius_usuario)} grados fahrenheit.")


'''
10. Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
'''
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    round_promedio = round(promedio, 2)
    return round_promedio
   
num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

print(f"El promedio es {calcular_promedio(num1, num2, num3)}.")