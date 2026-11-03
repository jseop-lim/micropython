# Test math.pow raising OverflowError when the result overflows

try:
    import math
except ImportError:
    print("SKIP")
    raise SystemExit

try:
    math.pow(10.0, 400)
except OverflowError:
    print("OverflowError")

try:
    math.pow(-10.0, 401)
except OverflowError:
    print("OverflowError")

# a zero base with a negative exponent is still a domain error
try:
    math.pow(0.0, -1)
except ValueError:
    print("ValueError")
