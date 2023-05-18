"""Implemente una clase bajo el patrón observer donde una serie de clases están 
subscriptas, cada clase espera que su propio ID (una secuencia arbitraria de 4 
caracteres) sea expuesta y emitirá un mensaje cuando el ID emitido y el propio 
coinciden. Implemente 4 clases de tal manera que cada una tenga un ID 
especifico. Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con 
ID para el que tenga una clase implementada"""

class Observer:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, emitted_id):
        if self.observer_id == emitted_id:
            print(f"ID coincidente encontrado: {self.observer_id}")


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, emitted_id):
        for observer in self.observers:
            observer.update(emitted_id)


# Clases específicas que heredan de Observer

class ClassA(Observer):
    def __init__(self):
        super().__init__("ID1")


class ClassB(Observer):
    def __init__(self):
        super().__init__("ID2")


class ClassC(Observer):
    def __init__(self):
        super().__init__("ID3")


class ClassD(Observer):
    def __init__(self):
        super().__init__("ID4")


# Crear instancia de Observable y agregar las clases observadoras

observable = Observable()
observable.add_observer(ClassA())
observable.add_observer(ClassB())
observable.add_observer(ClassC())
observable.add_observer(ClassD())

# Emitir 8 ID y notificar a las clases observadoras

emitted_ids = ["ID1", "ID2", "ID3", "ID4", "ID5", "ID6", "ID7", "ID8"]

for emitted_id in emitted_ids:
    observable.notify_observers(emitted_id)