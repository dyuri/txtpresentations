# Python Type Hints

## History

- 2008 python 3 introduced function annotations ([PEP-3107](https://www.python.org/dev/peps/pep-3107/))
- 2012 mypy appeared - optional static type checker based on function annotations
- 2015 "official" python type hints ([PEP-484](https://www.python.org/dev/peps/pep-0484/))
- 2016 variable annotations ([PEP-526](https://www.python.org/dev/peps/pep-0526/))
- Many (slightly different) static type checkers are available now:
  - mypy
  - pyre (by Facebook)
  - pytype (by Google)
  - pyright (by Microsoft) (+ pylance, but it isn't open source)
  - ...
- Dynamic (runtime) type checkers:
  - enforce
  - pydantic
  - pytypes
  - ...

## Function annotations

Function arguments and return value can be annotated by _anything_. 

```python
def a(x: "cica") -> 1+1:
    return x+1

a.__annotations__
{'return': 2, 'x': 'cica'}
```

And they can be used for anything too - documentation, type hinting, ...

## Type hints/checking

PEP was based on mypy, introducing "official" type variables with the `typing` module, generics, ..., but not the way how type checking should work.

For variables, type comments were defined (until PEP-528, but they are still available):

```python
x = []                 # type List[Employee]
x: List[Employee] = [] # same
```

Just as function annotations, they are not restricted to have types, can contain anything:

```python
a: "cica" = 12
__annotations__["a"] # "cica"
```

