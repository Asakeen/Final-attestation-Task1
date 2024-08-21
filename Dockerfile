# Используем базовый образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем файл app.py в контейнер
COPY app.py .

# Устанавливаем команду запуска
CMD ["python", "app.py", "Андрей"]
