# Test float power raising OverflowError when the result overflows

try:
    pow(2.0, 1024)
except OverflowError:
    print("OverflowError")

try:
    10.0**400
except OverflowError:
    print("OverflowError")

try:
    pow(-10.0, 401)
except OverflowError:
    print("OverflowError")

print(pow(float("inf"), 2))
print(pow(2.0, float("inf")))
