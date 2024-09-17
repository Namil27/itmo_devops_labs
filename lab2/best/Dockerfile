# Используем минимальный базовый образ.
FROM python:3.9-slim

# Устанавливаем необходимые зависимости, фиксируя их версии.
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем только нужные файлы, исключая ненужные через .dockerignore.
COPY . /app

WORKDIR /app
CMD ["python3", "app.py"]
