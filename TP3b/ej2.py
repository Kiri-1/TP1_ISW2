from abc import ABC, abstractmethod

class Laminador(ABC):
    """
    The Implementation defines the interface for all laminador classes.
    """
    @abstractmethod
    def producir_lamina(self) -> str:
        pass

class TrenLaminador5(Laminador):
    """
    Each Concrete Implementation corresponds to a specific laminador and implements
    the Laminador interface using that laminador's API.
    """
    def producir_lamina(self) -> str:
        return "Lámina de acero de 0.5\" de espesor y 5 mts de largo producida por el tren laminador de 5 mts."

class TrenLaminador10(Laminador):
    """
    Each Concrete Implementation corresponds to a specific laminador and implements
    the Laminador interface using that laminador's API.
    """
    def producir_lamina(self) -> str:
        return "Lámina de acero de 0.5\" de espesor y 10 mts de largo producida por el tren laminador de 10 mts."

class Lamina(ABC):
    """
    The Abstraction defines the interface for the "control" part of the two
    class hierarchies. It maintains a reference to an object of the
    Laminador hierarchy and delegates all of the real work to this object.
    """
    def __init__(self, laminador: Laminador) -> None:
        self.laminador = laminador

    def producir(self) -> str:
        return self.laminador.producir_lamina()

class LaminaAncha(Lamina):
    """
    You can extend the Abstraction without changing the Laminador classes.
    """
    def producir(self) -> str:
        return f"Lámina ancha: {self.laminador.producir_lamina()}"

if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured laminador-
    laminar combination.
    """
    laminador = TrenLaminador5()
    lamina = Lamina(laminador)
    print(lamina.producir())

    laminador = TrenLaminador10()
    lamina = LaminaAncha(laminador)
    print(lamina.producir())
