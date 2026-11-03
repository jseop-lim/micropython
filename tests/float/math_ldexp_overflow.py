# Test math.ldexp raising OverflowError when the result overflows

try:
    import math
except ImportError:
    print("SKIP")
    raise SystemExit

try:
    math.ldexp(1.0, 1024)
except OverflowError:
    print("OverflowError")

try:
    math.ldexp(-1.0, 1024)
except OverflowError:
    print("OverflowError")

print(math.ldexp(float("inf"), 1))
