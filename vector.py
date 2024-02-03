class Vector(list):
    @property
    def count(self) -> int:
        return len(self)

    def __str__(self) -> 'Vector':
        return f"{{\"data\": [{', '.join(str(v) for v in self)}]}}"

    def __copy__(self) -> 'Vector':
        return Vector(self)

    def __add__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(a + b for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(a + other for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    def __iadd__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError(f"Размеры данных векторов не совпадают {type(other)}")
            for i, v in enumerate(other):
                self[i] += v
            return Vector(self)
        if isinstance(other, float) or isinstance(other, int):
            for i in range(self.count):
                self[i] += other
            return Vector(self)
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    __radd__ = __add__

    def __sub__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(a - b for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(a - other for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    def __isub__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError(f"Размеры данных векторов не совпадают {type(other)}")
            for i, v in enumerate(other):
                self[i] -= v
            return Vector(self)
        if isinstance(other, float) or isinstance(other, int):
            for i in range(self.count):
                self[i] -= other
            return Vector(self)
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    def __rsub__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(b - a for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(other - a for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    def __mul__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(a * b for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(a * other for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    __imul__ = __add__

    def __rmul__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(b * a for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(other * a for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    def __truediv__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(a / b for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(a / other for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    def __rtruediv__(self, other) -> 'Vector':
        if isinstance(other, Vector):
            return Vector(*(b / a for a, b in zip(self, other)))
        if isinstance(other, float) or isinstance(other, int):
            return Vector(*(other / a for a in self))
        raise ValueError(f"Имеется непригодный тип данных {type(other)}")

    __itruediv__  = __truediv__
