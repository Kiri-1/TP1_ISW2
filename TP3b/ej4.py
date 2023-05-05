# *--------------------------------------------------
# * decorator.py
# * excerpt from https://refactoring.guru/design-patterns/decorator/python/example
# *--------------------------------------------------

class Component():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class Number(Component):
    """
    La clase Number es la clase base que se decorará. 
    """

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def __str__(self):
        return str(self._value)

    def operation(self) -> str:
        return self._value


class NumberDecorator(Component):
    """
    El decorador base tiene la misma interfaz que la clase Number.
    """
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    def get_value(self):
        return self._component.get_value()

    def __str__(self):
        return str(self._component)

    def operation(self) -> str:
        return self._component.operation()
    
    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.
        """
        return self._component

class AddTwoDecorator(NumberDecorator):
    """
    Suma dos al número original.
    """

    def get_value(self):
        return self.component.get_value() + 2

    def __str__(self):
        return str(self.get_value())

    def operation(self) -> str:
        return f"({self.component.operation()}) +2"


class MultiplyByTwoDecorator(NumberDecorator):
    """
    Multiplica el número original por dos.
    """

    def get_value(self):
        return self.component.get_value() * 2

    def __str__(self):
        return str(self.get_value())


    def operation(self) -> str:
        return f"({self.component.operation()}) *2"
    
class DivideByThreeDecorator(NumberDecorator):
    """
    Divide el número original por tres.
    """

    def get_value(self):
        return self.component.get_value() / 3

    def __str__(self):
        return str(self.get_value())

    def operation(self) -> str:
        return f"({self.component.operation()}) /3"

if __name__ == "__main__":
    value = int(input("Ingrese un número: "))
    number = Number(value)
    print("Número sin decorar:", number)

    # Agregar decoradores y mostrar resultados
    add_two = AddTwoDecorator(number)
    multiply_by_two = MultiplyByTwoDecorator(add_two)
    divide_by_three = DivideByThreeDecorator(multiply_by_two)

    print("Número con decoradores:", divide_by_three)
    print("Resultado de :", add_two.get_value())
    print("Resultado de :", multiply_by_two.get_value())
    print("Resultado de :", round(divide_by_three.get_value(), 2))

    print(f"RESULT: {divide_by_three.operation()}", end="")