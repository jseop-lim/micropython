# Test complex power raising OverflowError when the result overflows

try:
    complex
except NameError:
    print("SKIP")
    raise SystemExit

try:
    pow(-10.0, 400.5)
except OverflowError:
    print("OverflowError")

try:
    (-10 + 0j) ** 400.5
except OverflowError:
    print("OverflowError")

try:
    pow(2 + 0j, 2000)
except OverflowError:
    print("OverflowError")

try:
    (1e200 + 0j) ** 2
except OverflowError:
    print("OverflowError")
