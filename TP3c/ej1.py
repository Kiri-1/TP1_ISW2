"""Cree una clase bajo el patrón cadena de responsabilidad donde los números del 
1 al 100 sean pasados a las clases subscriptas en secuencia, aquella que 
identifique la necesidad de consumir el número lo hará y caso contrario lo 
pasará al siguiente en la cadena. Implemente una clase que consuma números 
primos y otra números pares. Puede ocurrir que un número no sea consumido 
por ninguna clase en cuyo caso se marcará como no consumido"""

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        if self.successor:
            return self.successor.handle(number)
        else:
            print(f"El número {number} no fue consumido.")

class PrimeHandler(Handler):
    def handle(self, number):
        if self.is_prime(number):
            print(f"Consumiendo número primo: {number}")
        else:
            super().handle(number)

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"Consumiendo número par: {number}")
        else:
            super().handle(number)

# Crear la cadena de responsabilidad
handler_chain = EvenHandler(PrimeHandler())

# Procesar los números del 1 al 100
for number in range(1, 101):
    handler_chain.handle(number)
