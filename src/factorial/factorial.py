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
        print("El factorial de un número negativo no existe")
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

if len(sys.argv) < 2:
    input_str = input("Por favor, ingrese el rango de números en el formato numero inicial hasta numero final: ")
    inicio, final = map(int, input_str.split('-'))
else:
    inicio, final = map(int, sys.argv[1].split('-'))

if inicio > final:
    inicio, final = final, inicio

print("Calculando los factoriales entre", inicio, "y", final, "...")

for num in range(inicio, final+1):
    print("El factorial de", num,"! es", factorial(num))