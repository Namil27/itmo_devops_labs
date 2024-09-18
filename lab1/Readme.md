# Лабораторная работа 1: Настройка Nginx с поддержкой нескольких доменов и SSL

## Ход работы:

1. **Создание шаблонов страниц:**
   Сначала были созданы шаблоны двух pet-проектов в виде HTML-страниц с разным содержанием. Один проект находился в
   папке `pet1`, другой — в `pet2`.

2. **Базовая настройка Nginx:**
   Был написан базовый конфиг Nginx, который отображал статические файлы при подключении к домену `localhost` по HTTP. В
   конфигурации использовался стандартный блок событий:

```nginx
events {
    worker_connections 1024;  # Максимальное количество соединений
}
```

3. **Оборачивание Nginx в контейнер:**
   Для упрощения развертывания на разных системах конфигурация Nginx была обернута в Docker-контейнер. Базовый конфиг
   Nginx был добавлен в `docker-compose.yml`:

```yaml
services:
  nginx:
    build:
      context: ./nginx
    container_name: nginx_server
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./nginx/keys:/etc/keys  # SSL сертификаты
      - ./pet1:/pet1  # Файлы проекта 1
      - ./pet2:/pet2  # Файлы проекта 2
    networks:
      - webnet
    extra_hosts:
      - "nelocalhost:127.0.0.1"  # Добавление домена nelocalhost в /etc/hosts
```

4. **Добавление второго домена:** В `docker-compose.yml` и конфигурации Nginx был добавлен второй домен `nelocalhost`,
   который вел на HTML-страничку второго pet-проекта. Для каждого домена был добавлен соответствующий блок конфигурации
   сервера в `nginx.conf`:

5. **Генерация самоподписанных SSL-сертификатов:** Для работы с HTTPS с помощью `openssl` были сгенерированы
   самоподписанные сертификаты для доменов `localhost` и `nelocalhost`. Команды для генерации:

```bash
openssl genpkey -algorithm RSA -out localhost.key -aes256
openssl req -new -key localhost.key -out localhost.csr
openssl x509 -req -days 365 -in localhost.csr -signkey localhost.key -out localhost.crt

openssl genpkey -algorithm RSA -out nelocalhost.key -aes256
openssl req -new -key nelocalhost.key -out nelocalhost.csr
openssl x509 -req -days 365 -in nelocalhost.csr -signkey nelocalhost.key -out nelocalhost.crt
```

6. **Настройка HTTPS и редиректа с HTTP:**В конфигурации Nginx были прописаны пути к SSL-сертификатам и добавлены блоки
   для редиректа с HTTP на HTTPS:

```nginx configuration
# Редирект с HTTP на HTTPS для localhost
server {
   listen 80;
   server_name localhost;

   # Редирект на HTTPS
   return 301 https://$host$request_uri;
}

# HTTPS сервер для localhost
server {
   listen 443 ssl;
   server_name localhost;

   ssl_certificate /etc/keys/localhost.crt;
   ssl_certificate_key /etc/keys/localhost.key;

   location / {
       root /pet1;
       index index.html;
       try_files $uri $uri/ =404;
   }
}
```

Аналогично был настроен сервер для `nelocalhost`, который обслуживает второй проект:

```nginx configuration
# HTTPS сервер для nelocalhost
server {
    listen 443 ssl;
    server_name nelocalhost;

    ssl_certificate /etc/keys/nelocalhost.crt;
    ssl_certificate_key /etc/keys/nelocalhost.key;

    location / {
        root /pet2;
        index index.html;
        try_files $uri $uri/ =404;
    }
}
```

7. **Тестирование работы:** После завершения настройки Docker Compose и Nginx была запущена сборка контейнеров, и оба
   сайта были протестированы по HTTPS.

## Вывод:

В результате выполнения лабораторной работы был настроен веб-сервер Nginx с поддержкой нескольких доменов и SSL, а также
реализован редирект с HTTP на HTTPS для обоих проектов.
