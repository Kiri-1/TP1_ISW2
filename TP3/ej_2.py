class Impuestos:
    # Singleton instance
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def calcular_impuestos(self, base_imponible):
        iva = 0.21 * base_imponible
        iibb = 0.05 * base_imponible
        contribuciones = 0.012 * base_imponible
        total_impuestos = iva + iibb + contribuciones
        return total_impuestos
# Obtener instancia del Singleton
impuestos = Impuestos.get_instance()

while True:
    base_imponible = float(input("Ingrese la base imponible para calcular los impuestos / ingrese 0 para salir: "))
    if base_imponible == 0:
        break
    total_impuestos = impuestos.calcular_impuestos(base_imponible)
    print("El total de impuestos a pagar es:", total_impuestos)
