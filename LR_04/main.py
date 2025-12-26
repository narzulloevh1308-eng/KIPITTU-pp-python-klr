import os
import json

# Контекстный менеджер safe_open
class safe_open:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, "r", encoding="utf-8")
        except FileNotFoundError:
            self.file = open(self.filename, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# Использование safe_open
with safe_open("test.txt") as f:
    try:
        content = f.read()
        print("Содержимое файла:")
        print(content)
    except Exception:
        print("Файл создан заново.")


# Поиск файлов по расширению
def find_files_by_extension(path, extension):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                result.append(os.path.join(root, file))
    return result


# Подсчёт размера каталога
def get_directory_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


# Сохранение результата в JSON
def save_result_to_json(data, filename="result.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# Запуск анализа
path = "."
files = find_files_by_extension(path, ".txt")
size = get_directory_size(path)

result = {
    "files_found": files,
    "total_size_bytes": size
}

save_result_to_json(result)

print("Результаты сохранены в result.json")
