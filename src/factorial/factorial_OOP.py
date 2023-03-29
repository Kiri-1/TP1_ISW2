#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        self.min = None
        self.max = None

    def factorial(self, num):
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

    def run(self, min=None, max=None):
        if not min and not max:
            input_ = input("Por favor, ingrese el rango de números en el formato inicio-final: ")
            self.min, self.max = map(int, input_.split('-'))
        else:
            self.min, self.max = min, max

        if self.min > self.max:
            self.min, self.max = self.max, self.min

        print("Calculando los factoriales entre", self.min, "y", self.max, "...")

        for num in range(self.min, self.max+1):
            print("El factorial de", num,"! es", self.factorial(num))
factorial = Factorial() 
factorial.run()
