# Test math functions raising OverflowError when the result overflows

try:
    import math

    math.cosh
except (ImportError, AttributeError):
    print("SKIP")
    raise SystemExit

try:
    math.exp(1000)
except OverflowError:
    print("OverflowError")

try:
    math.expm1(1000)
except OverflowError:
    print("OverflowError")

try:
    math.cosh(1000)
except OverflowError:
    print("OverflowError")

try:
    math.sinh(-1000)
except OverflowError:
    print("OverflowError")

try:
    math.gamma(200)
except OverflowError:
    print("OverflowError")

# the pole of gamma at zero is still a domain error
try:
    math.gamma(0)
except ValueError:
    print("ValueError")
