# test builtin hex function

print(hex(1))
print(hex(-1))
print(hex(15))
print(hex(-15))

print(hex(12345))
print(hex(0x12345))

# argument must be an integer, a tuple is not unpacked
try:
    hex((1,))
except TypeError:
    print("TypeError")
