# test round() with integral values

tests = [
    False, True,
    0, 1, -1, 10
]
for t in tests:
    print(round(t))

# ndigits=None is the same as omitting it
print(round(1, None))
