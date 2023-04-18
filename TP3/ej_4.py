class Factura:
    def __init__(self, builder):
        self.importe = builder.importe
        self.condicion_impositiva = builder.condicion_impositiva
        self.importe_total = builder.importe_total
        
    def __str__(self):
        return f"Factura de ${self.importe} ({self.condicion_impositiva}): ${self.importe_total}"
class FacturaBuilder:
    def __init__(self):
        self.importe = 0
        self.condicion_impositiva = ""
        self.importe_total = 0
        
    def set_importe(self, importe):
        self.importe = importe
        return self
    
    def set_condicion_impositiva(self, condicion_impositiva):
        self.condicion_impositiva = condicion_impositiva
        return self
    
    def calcular_importe_total(self):
        if self.condicion_impositiva == "IVA Responsable":
            iva = 0.21
            self.importe_total = self.importe * (1 + iva)
        elif self.condicion_impositiva == "IVA No Inscripto":
            self.importe_total = self.importe
        elif self.condicion_impositiva == "IVA Exento":
            self.importe_total = self.importe
        else:
            raise ValueError("La condición impositiva ingresada no es válida.")
        return self
    
    def build(self):
        self.calcular_importe_total()
        return Factura(self)
    
factura_builder = FacturaBuilder()
factura_builder.set_importe(float(input("Ingrese el importe de la factura: ")))
factura_builder.set_condicion_impositiva(input("Ingrese la condición impositiva de la factura /IVA Responsable/IVA No Inscripto/IVA Exento: "))
factura = factura_builder.build()
print(factura)
