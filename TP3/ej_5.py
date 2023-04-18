import os
class Body:
    shape = None

class Turbine:
    horsepower = None

class Wing:
    length = None

class LandingGear:
    type = None

class Builder:
    def getBody(self):
        pass

    def getTurbine(self):
        pass

    def getWing(self):
        pass

    def getLandingGear(self):
        pass
# Esta es la hoja de ruta para construir un avión
class AirplaneBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "Narrow Body"
        return body

    def getTurbine(self):
        turbine = Turbine()
        turbine.horsepower = 1500
        return turbine

    def getWing(self):
        wing = Wing()
        wing.length = 40
        return wing

    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Retractable"
        return landing_gear
    
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getAirplane(self):
        airplane = Airplane()

        # Primero el body
        body = self.__builder.getBody()
        airplane.setBody(body)

        # Luego las turbinas
        for i in range(2):
            turbine = self.__builder.getTurbine()
            airplane.attachTurbine(turbine)

        # Luego las alas
        for i in range(2):
            wing = self.__builder.getWing()
            airplane.attachWing(wing)

        # Finalmente el tren de aterrizaje
        landing_gear = self.__builder.getLandingGear()
        airplane.setLandingGear(landing_gear)

        # Retorna el avión completo
        return airplane

# Esta es la definición de un objeto avión inicializando todos sus atributos
class Airplane:
    def __init__(self):
        self.__turbines = []
        self.__wings = []
        self.__landing_gear = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachTurbine(self, turbine):
        self.__turbines.append(turbine)

    def attachWing(self, wing):
        self.__wings.append(wing)

    def setLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Body shape: %s" % (self.__body.shape))
        print("Turbine horsepower: %d" % (self.__turbines[0].horsepower))
        print("Wing length: %d" % (self.__wings[0].length))
        print("Landing gear type: %s" % (self.__landing_gear.type))

def main():
    airplaneBuilder = AirplaneBuilder()
    director = Director()
    director.setBuilder(airplaneBuilder)

