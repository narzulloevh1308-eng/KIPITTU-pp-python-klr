expenses = []

with open("data.txt") as f:
    for line in f:
        expenses.append(int(line.strip()))

limit = 300

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
    print("Нет периода с суммой ≥ лимита")
else:
    print("Минимальный период:", min_len, "дней")
