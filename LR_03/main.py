from collections import Counter

# Сообщения об ошибках
errors = [
    "SyntaxError: invalid syntax",
    "TypeError: unsupported operand type(s)",
    "NameError: name 'x' is not defined",
    "IndentationError: unexpected indent",
    "SyntaxError: missing parenthesis",
    "TypeError: can only concatenate str",
    "NameError: variable not defined"
]

# 1. Самые частые типы ошибок
error_types = [msg.split(":")[0] for msg in errors]
type_counts = Counter(error_types)

print("Частые типы ошибок:")
for err, count in type_counts.most_common():
    print(f"{err} — {count}")

# 2. Рейтинг слов в ошибках
words = []
for msg in errors:
    for w in msg.lower().replace(":", "").split():
        words.append(w)

word_counts = Counter(words)

print("\nРейтинг слов (топ-10):")
for word, count in word_counts.most_common(10):
    print(f"{word} — {count}")

# 3. Ошибки, характерные для новичков
newbie_errors_set = {"syntaxerror", "indentationerror", "nameerror"}
newbie_errors = []

for msg in errors:
    err_type = msg.split(":")[0].lower()
    if err_type in newbie_errors_set:
        newbie_errors.append(msg)

print("\nОшибки, характерные для новичков:")
for e in newbie_errors:
    print("-", e)from collections import Counter

# Сообщения об ошибках
errors = [
    "SyntaxError: invalid syntax",
    "TypeError: unsupported operand type(s)",
    "NameError: name 'x' is not defined",
    "IndentationError: unexpected indent",
    "SyntaxError: missing parenthesis",
    "TypeError: can only concatenate str",
    "NameError: variable not defined"
]

# 1. Самые частые типы ошибок
error_types = [msg.split(":")[0] for msg in errors]
type_counts = Counter(error_types)

print("Частые типы ошибок:")
for err, count in type_counts.most_common():
    print(f"{err} — {count}")

# 2. Рейтинг слов в ошибках
words = []
for msg in errors:
    for w in msg.lower().replace(":", "").split():
        words.append(w)

word_counts = Counter(words)

print("\nРейтинг слов (топ-10):")
for word, count in word_counts.most_common(10):
    print(f"{word} — {count}")

# 3. Ошибки, характерные для новичков
newbie_errors_set = {"syntaxerror", "indentationerror", "nameerror"}
newbie_errors = []

for msg in errors:
    err_type = msg.split(":")[0].lower()
    if err_type in newbie_errors_set:
        newbie_errors.append(msg)

print("\nОшибки, характерные для новичков:")
for e in newbie_errors:
    print("-", e)
