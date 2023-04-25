class Number:
    """
    La clase Number es la clase base que se decorará. 
    """

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def __str__(self):
        return str(self._value)


class NumberDecorator:
    """
    El decorador base tiene la misma interfaz que la clase Number.
    """

    def __init__(self, number: Number):
        self._number = number

    def get_value(self):
        return self._number.get_value()

    def __str__(self):
        return str(self._number)


class AddTwoDecorator(NumberDecorator):
    """
    Suma dos al número original.
    """

    def get_value(self):
        return self._number.get_value() + 2

    def __str__(self):
        return str(self.get_value())


class MultiplyByTwoDecorator(NumberDecorator):
    """
    Multiplica el número original por dos.
    """

    def get_value(self):
        return self._number.get_value() * 2

    def __str__(self):
        return str(self.get_value())


class DivideByThreeDecorator(NumberDecorator):
    """
    Divide el número original por tres.
    """

    def get_value(self):
        return self._number.get_value() / 3

    def __str__(self):
        return str(self.get_value())

if __name__ == "__main__":
    value = int(input("Ingrese un número: "))
    number = Number(value)
    print("Número sin decorar:", number)

    # Agregar decoradores y mostrar resultados
    add_two = AddTwoDecorator(number)
    multiply_by_two = MultiplyByTwoDecorator(add_two)
    divide_by_three = DivideByThreeDecorator(multiply_by_two)

    print("Número con decoradores:", divide_by_three)
    print("Resultado de AddTwoDecorator:", add_two.get_value())
    print("Resultado de MultiplyByTwoDecorator:", multiply_by_two.get_value())
    print("Resultado de DivideByThreeDecorator:", divide_by_three.get_value())