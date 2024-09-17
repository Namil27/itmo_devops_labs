# Использование тяжелого базового образа.
FROM ubuntu:latest

# Установка обновлений при каждом запуске контейнера.
RUN apt-get update && apt-get install -y python3

# Копирование всех файлов из текущей директории.
COPY . /app

WORKDIR /app
CMD ["python3", "app.py"]
