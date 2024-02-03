from common import NUMERICAL_FORMAT_4F as _4F, NUMERICAL_ACCURACY


def c_2_str(c):
    return f"{{\"re\": {c.real:{_4F}}, \"im\": {c.imag:{_4F}}}}"

# def build_in_vector():
    # import math
    # v1 = [1, 2, 3, 4, 5, 6, 7]
    # v2 = [7, 6, 5, 4, 3, 2, 1]
    # print(f"v1 + v2   = {map(sum, zip(v1, v2))}")
    # print(f"v1 - v2   = {list(set(v2) - set(v1))}")
    # print(f"v1 * v2   = {v1 * v2}")
    # print(f"v1 / v2   = {v1 / v2}")

def my_vector():
    from vector import Vector
    v1 = [1, 2, 3, 4, 5, 6, 7]
    v2 = [7, 6, 5, 4, 3, 2, 1]
    print(f"v1 + v2   = {Vector(v1) + Vector(v2)}")
    print(f"v1 - v2   = {Vector(v1) - Vector(v2)}")
    print(f"v1 * v2   = {Vector(v1) * Vector(v2)}")
    print(f"v1 / v2   = {Vector(v1) / Vector(v2)}")

# def build_in_complex():
    # c1 = complex(1, 2)
    # c2 = complex(2, -1)
    # import cmath
    # print(f"arg(c2)   = {cmath.phase(c2)}")
    # print(f"mod(c2)   = {abs(c2)}")
    # print(f"exp(c2)   = {c_2_str(cmath.exp(c2))}")
    # print(f"pow(c2)   = {c_2_str(c2**2.33)}")
    # print(f"sin(c2)   = {cmath.sin(c2)}")
    # print(f"cos(c2)   = {cmath.cos(c2)}")
    # print(f"tan(c2)   = {cmath.tan(c2)}")

    #print(f"c1: {c1}")
    #print(f"c2: {c2}")
    #print(f'c1 + c2 = {c1 + c2}')
    #print(f'c1 * c2 = {c1 * c2}')
    #print(f'c1 / c2 = {c1 / c2}')
    #print(f'c1 + 2 = {c1 + 2}')
    #print(f'c1 * 2 = {c1 * 2}')
    #print(f'c1 / 2 = {c1 / 2}')
    #print(f'2 + c1 = {2 + c1}')
    #print(f'2 * c1 = {2 * c1}')
    #print(f'2 / c1 = {2 / c1}')


# def my_complex():
#     from complex import Complex
#     c1 = Complex(1, 2)
    # c2 = Complex(2, -1)
    # print(f"conj(c2)  = {Complex.conjugate(c2)}")
    # print(f"arg(c2)   = {Complex.phase(c2)}")
    # print(f"mod(c2)   = {Complex.module(c2)}")
    # print(f"exp(c2)   = {Complex.exponent(c2)}")
    # print(f"pow(c2)   = {Complex.power(c2, 2.33)}")
    # print(f"sin(c2)   = {Complex.sin(c2)}")
    # print(f"cos(c2)   = {Complex.cos(c2)}")
    # print(f"tan(c2)   = {Complex.tan(c2)}")


    #print(f"c1: {c1}")
    #print(f"c2: {c2}")
    #print(f'c1 + c2 = {c1 + c2}')
    #print(f'c1 * c2 = {c1 * c2}')
    #print(f'c1 / c2 = {c1 / c2}')
    #print(f'c1 + 2 = {c1 + 2}')
    #print(f'c1 * 2 = {c1 * 2}')
    #print(f'c1 / 2 = {c1 / 2}')
    #print(f'2 + c1 = {2 + c1}')
    #print(f'2 * c1 = {2 * c1}')
    #print(f'2 / c1 = {2 / c1}')


if __name__ == "__main__":
    # build_in_vector()
    print('')
    my_vector()
