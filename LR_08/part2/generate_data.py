import random

expenses = [random.randint(10, 200) for _ in range(30)]

with open("data.txt", "w") as f:
    for x in expenses:
        f.write(str(x) + "\n")

print("Файл data.txt создан")
