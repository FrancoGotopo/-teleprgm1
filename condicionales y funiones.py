#una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones

from math import pi
 
r = float (input("Escriba el radio del circulo"))

area = pi * r **2

print("El área del circulo es{}".format(area))

#una función en python que acepte 3 valores y devuelva solo el maximo de los tres.

def Nota(alumno1, alumno2, alumno3):
    suma = alumno1 + alumno2 + alumno3
    return suma

media = Nota(17, 8, 14)
print("El valor de los Tres es:",media )

# Dado una lista de enteros, defina una función en python que devuelva la suma de solo los valores impares de dicha lista.

def valores(valor1, valor2, valor3, valor4, valor5):
    suma = valor1 + valor2 + valor3 + valor4 + valor5
    return valor2 + valor3 + valor5

resultado = valores(12, 5, 7, 8, 15)
print("Resultado de la operacion es:",resultado )