def serial_sum(*args):
    if len(args) == 1:
        n = args[0]
        return sum(range(1, n + 1))
    elif len(args) == 2:
        start, end = args
        return sum(range(start, end + 1))

print(serial_sum(4))  # Output will be 10
print(serial_sum(2, 4))  # Output will be 9
