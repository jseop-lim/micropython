# tests for things that only Python 3.6 supports, needing floats

# underscores in numeric literals
print(1_000.1_8)
print("%.2g" % 1e1_2)

# underscore supported by int/float constructors
print(float("1_2_3"))
print(float("1_2_3.4"))
print("%.2g" % float("1e1_3"))


# underscores must sit between two digits
def test(s):
    try:
        print(float(s))
    except ValueError:
        print("ValueError")


test("_1")
test("1_")
test("1__0")
test("_")
test("1_.5")
test("1._5")
test("1e_5")
test("1_e5")
