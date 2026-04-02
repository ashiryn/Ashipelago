import os
import abc
from typing import Any


class AMeta(abc.ABCMeta):

    def __new__(mcs, name: str, bases: tuple[type, ...], attrs: dict[str, Any]):
        print("AMeta")
        cls = super().__new__(mcs, name, bases, attrs)
        return cls


class BMeta(AMeta):

    def __new__(mcs, name: str, bases: tuple[type, ...], attrs: dict[str, Any]):
        print("BMeta")
        attrs["a"] = 45
        cls = super().__new__(mcs, name, bases, attrs)
        return cls


class A(metaclass=AMeta):
    a = 0


class B(A, metaclass=BMeta):
    b = 0


class C(B):
    c = 0


if __name__ == "__main__":
    print(B.a)
