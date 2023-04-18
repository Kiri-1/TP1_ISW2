class Factorial:
    # Singleton instancia
    _instance = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
# Obtener instancia del Singleton
fact = Factorial.get_instance()
while True:
    print("Calcular factorial")
    entrada = input("Ingrese un número entero positivo / cadena vacía para salir): ")
    if entrada == "":
        break
    # Convertir entrada a entero y calcular factorial
    try:
        n = int(entrada)
        print(f"El factorial de {n} es {fact.factorial(n)}")
    except ValueError:
        print("Debe ingresar un número entero positivo")
print("Fin")