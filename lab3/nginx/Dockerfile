# Используем официальный образ Nginx
FROM nginx:latest

# Копируем файл конфигурации Nginx в контейнер
COPY nginx.conf /etc/nginx/nginx.conf

# Указываем рабочую директорию
WORKDIR /usr/share/nginx

# Открываем 80 порт для входящих запросов
EXPOSE 80

# Запускаем Nginx в режиме, когда он не уходит в фоновый процесс
CMD ["nginx", "-g", "daemon off;"]