from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Optionally, the base Component can declare an interface for setting and
        accessing a parent of the component in a tree structure. It can also
        provide some default implementation for these methods.
        """

        self._parent = parent

    """
    In some cases, it would be beneficial to define the child-management
    operations right in the base Component class. This way, you won't need to
    expose any concrete component classes to the client code, even during the
    object tree assembly. The downside is that these methods will be empty for
    the leaf-level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that lets the client code figure out whether a
        component can bear children.
        """

        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Leaf(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.
    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """

    def __init__(self, name: str) -> None:
        self._name = name

    def operation(self) -> str:
        return f"Leaf {self._name}"


class Composite(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, name: str) -> None:
        self._name = name
        self._children: List[Component] = []

    """
    A composite object can add or remove other components (both simple or
    complex) to or from its child list.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The Composite executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the composite's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"{self._name}({'+'.join(results)})"

def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """

    print(f"RESULT: {component.operation()}\n")

    if component.is_composite():
        for child in component._children:
            client_code(child)

if __name__ == "__main__":
    # Creación del producto principal
    product = Composite("Main product")

    # Creación de los tres subconjuntos con cuatro piezas cada uno
    subset1 = Composite("Subset 1")
    subset1.add(Leaf("Piece 1"))
    subset1.add(Leaf("Piece 2"))
    subset1.add(Leaf("Piece 3"))
    subset1.add(Leaf("Piece 4"))

    subset2 = Composite("Subset 2")
    subset2.add(Leaf("Piece 5"))
    subset2.add(Leaf("Piece 6"))
    subset2.add(Leaf("Piece 7"))
    subset2.add(Leaf("Piece 8"))

    subset3 = Composite("Subset 3")
    subset3.add(Leaf("Piece 9"))
    subset3.add(Leaf("Piece 10"))
    subset3.add(Leaf("Piece 11"))
    subset3.add(Leaf("Piece 12"))

    # Creación del subconjunto opcional
    optional_subset = Composite("Optional subset")
    optional_subset.add(Leaf("Optional piece 1"))
    optional_subset.add(Leaf("Optional piece 2"))
    optional_subset.add(Leaf("Optional piece 3"))
    optional_subset.add(Leaf("Optional piece 4"))

    # Añadir los subconjuntos al producto principal
    product.add(subset1)
    product.add(subset2)
    product.add(subset3)

    # Mostrar el producto principal con sus subconjuntos y piezas
    client_code(product)

    # Añadir el subconjunto opcional al subconjunto 2
    subset2.add(optional_subset)

    # Mostrar de nuevo el producto principal con el subconjunto opcional añadido
    client_code(product)