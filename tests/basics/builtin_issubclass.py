# test builtin issubclass

class A:
    pass

print(issubclass(A, A))
print(issubclass(A, (A,)))

try:
    issubclass(A, 1)
except TypeError:
    print('TypeError')

try:
    issubclass('a', 1)
except TypeError:
    print('TypeError')

# nested tuples of classes
print(issubclass(A, ((A,),)))
print(issubclass(A, (int, (str, (A,)))))
print(isinstance(A(), ((A,),)))

# arg 1 is not checked when there is no class to compare against
print(issubclass('a', ()))
print(issubclass('a', ((),)))

# every element of the tuple must be a class, up to the first match
print(issubclass(A, (A, 1)))

try:
    issubclass(A, (1,))
except TypeError:
    print('TypeError')

try:
    isinstance(1, (A, 1))
except TypeError:
    print('TypeError')
