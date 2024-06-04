def gcd(a: int, b: int) -> int:
    """Greatest common divisor through Euclides Algorithm"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Least common multiple throught Euclides Algorithm"""
    return a * b // gcd(a, b)
