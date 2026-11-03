# test builtin bool with user-defined __bool__

class A:
    def __bool__(self):
        return False


print(bool(A()))


class B:
    def __bool__(self):
        return "x"


try:
    bool(B())
except TypeError:
    print("TypeError")


class C:
    def __bool__(self):
        return 1


try:
    bool(C())
except TypeError:
    print("TypeError")


try:
    not C()
except TypeError:
    print("TypeError")


try:
    all([C()])
except TypeError:
    print("TypeError")
