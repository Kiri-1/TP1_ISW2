from abc import ABC, abstractmethod

class Hamburguesa(ABC):
    def entregar(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        print("La hamburguesa está lista para ser retirada en mostrador.")

class HamburguesaRetiro(Hamburguesa):
    def entregar(self):
        print("La hamburguesa está lista para ser retirada por el cliente.")

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        print("La hamburguesa será entregada a domicilio.")

class HamburguesaFactory:
    @staticmethod
    def crear_hamburguesa():
        tipo = input("Especifique el tipo de entrega (mostrador/retiro/delivery): ")
        if tipo == "mostrador":
            return HamburguesaMostrador()
        elif tipo == "retiro":
            return HamburguesaRetiro()
        elif tipo == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError(f"Tipo de hamburguesa inválido: {tipo}")
hamburguesa = HamburguesaFactory.crear_hamburguesa()
hamburguesa.entregar()  # imprimirá el mensaje correspondiente según el tipo de entrega especificado por el usuario
