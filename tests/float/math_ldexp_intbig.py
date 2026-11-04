# Test math.ldexp with an exponent outside the range of a C int

try:
    import math
except ImportError:
    print("SKIP")
    raise SystemExit

try:
    math.ldexp(1.0, 2**32)
except OverflowError:
    print("OverflowError")

print(math.ldexp(1.0, -(2**32)))
