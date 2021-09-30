from typing import List, TypeVar

T = TypeVar('T')
a: List[int] = []


def c(lista: List[T]) -> T:
    return lista[0]


def d(lista: List[T]) -> T:
    return str(lista[0])


a.append(1)
a.append(c([1]))
a.append(c(["alma"]))
