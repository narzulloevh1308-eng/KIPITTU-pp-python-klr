# Задача 1. Рекурсивное «сплющивание» вложенного списка
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


data = [1, [2, [3, 4]], 5]
print("Результат flatten:", flatten(data))


# Задача 2. Sliding Window — самая длинная подстрока без повторений
def longest_unique_substring(s):
    seen = {}
    left = 0
    max_len = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


print("abcabcbb →", longest_unique_substring("abcabcbb"))
print("pwwkew →", longest_unique_substring("pwwkew"))
print("bbbbb →", longest_unique_substring("bbbbb"))
