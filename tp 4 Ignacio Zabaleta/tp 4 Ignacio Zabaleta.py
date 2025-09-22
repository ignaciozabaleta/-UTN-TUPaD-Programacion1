'''
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
'''
num = 0
for num in range(0,101):
    print(num)


'''
2)Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. 
'''
num = int(input("Ingrese un numero entero"))
contador = 0
while num > 0:
    num = num // 10
    contador = contador + 1
print("El numero tiene",contador,"cifras")


'''
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = 0
for numero in range(num1 + 1, num2):
    suma = suma + numero
 
print(f"La suma de los números entre {num1} y {num2} es: {suma}")


'''
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. 
'''
num = 1
contador = 0
while num != 0:
        num = int(input("Ingrese un numero entero"))
        contador = contador + num
print("El total acumulado es", contador)


'''
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente.
'''
num = 100
for num in range(100,-2,-2):
    print(num)


'''
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario.
'''
num1 = int(input("Ingrese un numero entero"))
cont = 0

for num1 in range(0,num1+1,1):
    cont = cont + num1

print("La suma desde cero hasta el numero ingresado es de",cont)


'''
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
'''

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(1, 11):
    numero = int(input(f"Ingrese el número #{i}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print("Cantidad de números pares: ", pares)
print("Cantidad de números impares: ", impares)
print("Cantidad de números positivos: ", positivos)
print("Cantidad de números negativos: ", negativos)


'''
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). 
'''

suma = 0

for i in range(1, 101):
    numero = int(input(f"Ingrese el número #{i}: "))
    suma = suma + numero

media = suma/100

print("La media de los numeros ingresados es: ", media)


'''
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
'''