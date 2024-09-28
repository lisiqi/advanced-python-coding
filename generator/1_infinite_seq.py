def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 5

values = infinite_sequence()
for i in range(100):
    print(next(values))