def running_sum(numbers):
    total = 0
    for x in numbers:
        total += x
        yield total
