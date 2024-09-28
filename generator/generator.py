# Sequence of numbers 1 to 9,000,000
import sys
def mygenerator(n):
    for x in range(n):
        yield x**3

values = mygenerator(9000000)

print(next(values))
print(next(values))
print(next(values))

print(sys.getsizeof(values)) # 208 bytes, no matter how big n is

