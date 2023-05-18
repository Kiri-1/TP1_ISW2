"""Modifique el programa IS2_taller_memory.py para que la clase tenga la 
capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los 
mismos en cualquier orden de ser necesario. El método undo deberá tener un 
argumento adicional indicando si se desea recuperar el inmediato anterior (0) y 
los anteriores a el (1,2,3)."""

import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        if len(self.history) == 4:
            self.history.pop(0)  
        self.history.append(Memento(self.file, self.content))

    def undo(self, index):
        if index < len(self.history):
            memento = self.history[-index - 1]
            self.file = memento.file
            self.content = memento.content

    def print_content(self):
        print(self.content + "\n\n")


class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, index):
        writer.undo(index)


if __name__ == '__main__':
    os.system("clear")
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    writer.write("Clase de IS2 en UADER\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones\n")
    caretaker.save(writer)

    writer.write("Más contenido\n")
    caretaker.save(writer)

    writer.write("Otro contenido\n")
    caretaker.save(writer)

    writer.print_content()

    caretaker.undo(writer, 0)
    writer.print_content()

    caretaker.undo(writer, 2)
    writer.print_content()

    caretaker.undo(writer, 3)
    writer.print_content()