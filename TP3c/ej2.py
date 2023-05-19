
"""Implemente una clase bajo el patrón iterator que almacene una cadena de 
caracteres y permita recorrerla en sentido directo y reverso."""

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""

class StringIterator:
    def __init__(self):
        self.data = ""
        self.index = 0
        self.reverse = False

    def set_data(self, data):
        self.data = data
        self.index = 0

    def set_reverse(self, reverse):
        self.reverse = reverse
        self.index -= 1

    def has_next(self):
        if self.reverse:
            return self.index >= 0
        else:
            return self.index < len(self.data)

    def next(self):
        if self.has_next():
            if self.reverse:
                char = self.data[self.index]
                self.index -= 1
            else:
                char = self.data[self.index]
                self.index += 1
            return char
        else:
            return None


# Ejemplo de uso
if __name__ == '__main__':
    string_iterator = StringIterator()

    # Ingresar la cadena de caracteres por consola
    data = input("Ingresa una cadena de caracteres: ")
    string_iterator.set_data(data)

    print("Recorrido en sentido directo:")
    while string_iterator.has_next():
        char = string_iterator.next()
        print(char)

    print("\nRecorrido en sentido reverso:")
    string_iterator.set_reverse(True)
    while string_iterator.has_next():
        char = string_iterator.next()
        print(char)