# Test math.ldexp with an exponent too negative for a machine word

try:
    import math
except ImportError:
    print("SKIP")
    raise SystemExit

print(math.ldexp(1.0, -(2**64)))
print(math.ldexp(-1.0, -(2**64)))
print(math.ldexp(float("inf"), -(2**64)))
