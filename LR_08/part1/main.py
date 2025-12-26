def min_period(expenses, limit):
    left = 0
    current_sum = 0
    min_len = float("inf")

    for right in range(len(expenses)):
        current_sum += expenses[right]

        while current_sum >= limit:
            min_len = min(min_len, right - left + 1)
            current_sum -= expenses[left]
            left += 1

    if min_len == float("inf"):
        return 0

    return min_len


print(min_period([100, 200, 150, 80, 90], 300))
print(min_period([500, 100, 50], 400))
print(min_period([50, 60, 70], 500))
print(min_period([200], 200))
