''' 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
'''
print(f"Hola Mundo!")


'''2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. 
'''
nombre = input("Ingrese su nombre")
print(f"Hola {nombre}!")


'''3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla. 
'''
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = input("Ingrese su edad en años")
residencia = input("Ingrese su pais de residencia")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


'''4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro. 
'''
radio = int(input("Ingrese el radio de un circulo"))
area = 3.14 * radio ** 2
perimetro = 2*3.14*radio
print(f"El area es {area} y el perimetro es {perimetro}")


'''5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale. 
'''
segundos = int(input("Ingrese una cantidad de segundos"))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
print(f"{str(horas).zfill(2)}:{str(minutos).zfill(2)}")


'''6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número.
'''
num = int(input("Ingrese un numero del 1 al 10"))
for i in range(1, 11):
    resultado = num * i
    print(f"{num} * {i} = {resultado}")


'''7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
'''
num1 = int(input("Ingrese un numero distinto de cero"))
num2 = int(input("Ingrese un numero distinto de cero"))                 
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2
print(f"{num1} + {num2} = {suma}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} - {num2} = {resta}")


'''8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal. 
'''
peso = (float(input("Ingrese su peso en kilos")))
altura = (float(input("Ingrese su altura en metros")))              
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es {imc}") 


'''9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. 
'''
tempcelsius = (int(input("Ingrese una temperatura en grados celsius")))
fahrenheit = (tempcelsius*9/5)+32              
print(f"La temperatura en fahrenheit es {fahrenheit}") 


'''10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números. 
'''
num1 = (int(input("Ingrese un primer numero")))
num2 = (int(input("Ingrese un segundo numero")))
num3 = (int(input("Ingrese un tercer numero")))   
prom = (num1 + num2 + num3)/3          
print(f"El promedio es {prom}") 

