# Задача 1. Two Pointers — поиск пары с заданной суммой
def find_pair(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return numbers[left], numbers[right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return None


numbers = [10, 20, 30, 40, 50]
print("Пара с суммой 70:", find_pair(numbers, 70))


# Задача 2. Проверка палиндрома
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


print("level — палиндром:", is_palindrome("level"))
print("server — палиндром:", is_palindrome("server"))


# Задача 3. Сортировка данных
servers = [
    ("alpha", 30),
    ("beta", 10),
    ("gamma", 20)
]

print("\nСортировка по отклику:")
print(sorted(servers, key=lambda x: x[1]))

print("Сортировка по имени:")
print(sorted(servers, key=lambda x: x[0]))


# Задача 4. Линейный поиск
def linear_search(data, name):
    for server, response in data:
        if server == name:
            return response
    return None


print("\nОтклик сервера beta:", linear_search(servers, "beta"))
