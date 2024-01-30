from common import NUMERICAL_FORMAT_4F as _4F, NUMERICAL_ACCURACY
from collections import namedtuple
import math


class Complex(namedtuple('Complex', 're, im')):

    __slots__ = ()

    def __new__(cls, re: float = 0.0, im: float = 0.0) -> 'Complex':
        return super().__new__(cls, float(re), float(im))

    def __copy__(self) -> 'Complex':
        return Complex(*(e for e in self))

    def __str__(self) -> str:
        return f"{{\"re\": {self.re:{_4F}}, \"im\": {self.im:{_4F}}}}"

    def __neg__(self) -> 'Complex':
        return Complex(*(-e for e in self))

    def __abs__(self) -> float:
        return math.sqrt(sum(e * e for e in self))

    def __add__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(*(s + o for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)
        raise RuntimeError(f"Add::wrong argument type {type(other)}")

    __iadd__ = __add__

    __radd__ = __add__

    def __sub__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(*(s - o for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re - other, self.im)
        raise RuntimeError(f"Sub::wrong argument type {type(other)}")

    def __rsub__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(*(o - s for s, o in zip(self, other)))
        if isinstance(other, int) or isinstance(other, float):
            return Complex(other - self.re, self.im)
        raise RuntimeError(f"Sub::wrong argument type {type(other)}")

    __isub__ = __sub__

    def __mul__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(s * other for s in self))
        raise RuntimeError(f"Mul::wrong argument type {type(other)}")

    __imul__ = __mul__

    __rmul__ = __mul__

    def __truediv__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            denum = 1.0 / (other.re * other.re + other.im * other.im)
            return Complex((self.re * other.re + self.im * other.im) * denum,
                           (self.im * other.re - self.re * other.im) * denum)
        if isinstance(other, int) or isinstance(other, float):
            return Complex(*(s / other for s in self))
        raise RuntimeError(f"Div::wrong argument type {type(other)}")

    def __rtruediv__(self, other) -> 'Complex':
        if isinstance(other, Complex):
            denum = 1.0 / (self.re * self.re + self.im * self.im)
            return Complex((self.re * other.re + self.im * other.im) * denum,
                           (-self.im * other.re + self.re * other.im) * denum)
        if isinstance(other, int) or isinstance(other, float):
            mag = 1.0 / sum(elem * elem for elem in self)
            return Complex(other * self.re * mag, - other * self.im * mag)
        raise RuntimeError(f"Div::wrong argument type {type(other)}")

    def __eq__(self, other):
        if not isinstance(other, Complex):
            return False
        return not any(abs(left - right) > NUMERICAL_ACCURACY for left, right in zip(self, other))

    @staticmethod
    def phase(number: 'Complex') -> float:
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        if number.re > 0 or number.im != 0:
            return 2.0 * math.atan2(number.im, number.re + Complex.module(number))
        if number.re < 0 or number.im == 0:
            return math.pi
        return 1e32

    @staticmethod
    def module(number) -> float:
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        return abs(number)

    @staticmethod
    def exponent(number) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        e = math.exp(number.re)
        return Complex(e * math.cos(number.im), e * math.sin(number.im))

    @staticmethod
    def power(number, power) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        r = math.pow(Complex.module(number), power)
        a = Complex.phase(number)
        return Complex(r * math.cos(a * power), r * math.sin(a * power))

    @staticmethod
    def conjugate(number) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        return Complex(number.re, -number.im)

    @staticmethod
    def sqrt(number) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        r = math.sqrt(Complex.module(number))
        a = Complex.phase(number)
        return Complex(r * math.cos(a * 0.5), r * math.sin(a * 0.5))

    @staticmethod
    def sin(number) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        left = Complex.exponent(Complex(number.im, -number.re))
        rght = Complex.exponent(Complex(-number.im, number.re))
        return Complex(-(left.im - rght.im) * 0.5, (left.re - rght.re) * 0.5)

    @staticmethod
    def cos(number) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        left = Complex.exponent(Complex(number.im, -number.re))
        rght = Complex.exponent(Complex(-number.im, number.re))
        return Complex((left.re + rght.re) * 0.5, (left.im + rght.im) * 0.5)

    @staticmethod
    def tan(number) -> 'Complex':
        assert isinstance(number, Complex), f"Wrong type of input argument. Argument type is {type(number)}"
        left = Complex.exponent(Complex(number.im, -number.re))
        rght = Complex.exponent(Complex(-number.im, number.re))
        y = (Complex(-(left.im - rght.im), (left.re - rght.re))) / (Complex(-(left.im + rght.im), (left.re + rght.re)))
        return Complex(-y.im, y.re)



    # any
    # all
    # zip
    # *