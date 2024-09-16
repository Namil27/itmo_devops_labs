# Используем официальный образ Nginx
FROM nginx:latest


# Копируем файл конфигурации Nginx в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Указываем рабочую директорию
WORKDIR /usr/share/nginx/text

# Открываем 80 порт для входящих запросов
EXPOSE 80

CMD ["tail", "-f", "/dev/null"]

