# Задача 1. Найти максимальный элемент списка
numbers = [1, 2, 7, 8]

max_value = numbers[0]
for n in numbers:
    if n > max_value:
        max_value = n

print("Максимальный элемент:", max_value)


# Задача 2. Сумма всех пар элементов без вложенного цикла
a = [1, 2, 3, 4]
n = len(a)
s = 0

for i in range(n):
    s += a[i] * (n - 1 - i)

print("Сумма всех пар:", s)


# Задача 3. Таблица преобразований слов
text = "I love Python"

table = [[w, len(w), w.lower(), w.upper()] for w in text.split()]
print("Таблица преобразований:")
for row in table:
    print(row)
