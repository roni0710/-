from common import NUMERICAL_FORMAT_4F as _4F
from collections import namedtuple
import numpy as np
import math

class Complex(namedtuple('Complex', 'x, y')):

    __slots__ = ()

    def __new__(cls, x: float = 1.3, y: float = 2.4):
        return super().__new__(cls, float(x), float(y))

    def __init__(self):
        self.x = 1.3
        self.y = 2.4

    def __str__(self):
        return f"{{\"x\": {self.x:{_4F}}, \"y\": {self.y:{_4F}}}}"

    def __neg__(self):
        return Complex(*(val for val in self))

    def __sqrt__(self):
        return Complex(math.sqrt((self.x) + (self.y)))

    def __abs__(self):
        return Complex(math.sqrt((self.x) * (self.x) + (self.y) * (self.y)))

    def __pow__(self):
        return Complex(pow(self.x) + (self.y))

    def __conj__(self):
        return Complex(np.conj(self.x), np.conj(self.y))

    def __arg__(self):
        return Complex((self.y)/(self.x))

    __tan__ = __arg__

    def __sin__(self):
        return Complex((self.y)/math.sqrt((self.x) * (self.x) + (self.y) * (self.y)))

    def __cos__(self):
        return Complex((self.x)/math.sqrt((self.x) * (self.x) + (self.y) * (self.y)))

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(*(s + o for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(s + other for s in self))
        raise RuntimeError(f"Add::wrong argument type {type(other)}")

    __iadd__ = __add__

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(*(s - o for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(s - other for s in self))
        raise RuntimeError(f"Sub::wrong argument type {type(other)}")

    __rsub__ = __sub__

    __isub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(*(s * o for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(s * other for s in self))
        raise RuntimeError(f"Mul::wrong argument type {type(other)}")

    __imul__ = __mul__

    __rmul__ = __mul__

    def __div__(self, other):
        if isinstance(other, Complex):
            return Complex(*(s / o for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(s / other for s in self))
        raise RuntimeError(f"Div::wrong argument type {type(other)}")

    def __rdiv__(self, other):
        if isinstance(other, Complex):
            return Complex(*(o / s for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(other / s for s in self))
        raise RuntimeError(f"Div::wrong argument type {type(other)}")

    def __eq__(self, other):
        if (self.x != other.x):
            return False
        if (self.y != other.y):
            return False
        else:
            return True

    def __le__(self, other):
        if (abs(self.x) <= abs(other.x)):
            return True
        else:
            return False

    def __ge__(self, other):
        if (abs(self.x) >= abs(other.x)):
            return True
        else:
            return False
