import os
import sys
from datetime import datetime

# Определение пути
"""
1. Раскомментируйте следующую строку и введите желаемый путь.
Или оставьте всё как есть, и скрипт выполнится для корневого
каталога Вашей файловой ситемы.
2. При запуске скрипта в Windows, указывайте путь, используя
обратные слеши.
При запуске скрипта в Unix-подобных системах при указании пути 
используйте прямые слеши.
3. Убедитесь в наличии соответствующих разрешений доступа к 
файлам! Могут возникнуть ошибки при попытке их прочитать!

"""
# path = "/your/default/path"
path = os.path.abspath(os.sep)  # Корневой каталог по умолчанию

# Функция для вычисления количества файлов


def count_files(directory):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count

# Функция для получения топ-10 файлов по размеру


def top_10_files(directory):
    file_sizes = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Проверка на существование файла. Необходима, поскольку возникают проблемы из-за временных файлов.

            if os.path.exists(file_path):
                file_sizes.append(
                    (file, os.path.getsize(file_path) / 1024))  # Размер в Кб
    file_sizes.sort(key=lambda x: x[1], reverse=True)
    return file_sizes[:10]


# Приветственное сообщение


def greeting(name):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Привет, {name}! Текущее время: {current_time}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "Дружище"

    print(greeting(name))
    print(f"Общее количество файлов в директории '{
          path}': {count_files(path)}")
    print("Топ-10 файлов по размеру:")
    for file, size in top_10_files(path):
        print(f"{file}: {size:.2f} Кб")
