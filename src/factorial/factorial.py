#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num):
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1 
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2: #Modificación al programa para que si se omite el número como argumento lo solicite # Aumento la cantidad de argumentos para que no sea vacio
    num = int(input("Ingrese un número para calcular su factorial: "))
else:
    num = int(sys.argv[1])

print("Factorial", num, "! es", factorial(num))


