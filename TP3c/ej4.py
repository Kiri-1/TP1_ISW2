"""Modifique el programa IS2_taller_scanner.py para que además la secuencia de 
barrido de radios que tiene incluya la sintonía de una serie de frecuencias 
memorizadas tanto de AM como de FM. Las frecuencias estarán etiquetadas 
como M1, M2, M3 y M4. Cada memoria podrá corresponder a una radio de AM 
o de FM en sus respectivas frecuencias específicas. En cada ciclo de barrido se 
barrerán las cuatro memorias."""

import os


class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f"Sintonizando... Estación {self.stations[self.pos]} {self.name}")

    def scan_memories(self):
        for memory in self.memories:
            print(f"Sintonizando... Frecuencia de memoria {memory}")


class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"
        self.memories = ["M1", "M2", "M3", "M4"]

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan_memories(self):
        super().scan_memories()


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"
        self.memories = ["M1", "M2", "M3", "M4"]

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan_memories(self):
        super().scan_memories()


class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

    def scan_memories(self):
        self.state.scan_memories()


if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3 + [radio.scan_memories]
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()