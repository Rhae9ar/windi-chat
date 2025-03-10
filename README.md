# WinDI Chat API

Тестовое задание для компании WinDI.

## Описание проекта

Этот проект представляет собой реализацию чат-приложения с использованием FastAPI, WebSocket и PostgreSQL.

## Функциональные требования

- Подключение пользователей через WebSocket.
- Обмен текстовыми сообщениями в реальном времени.
- Создание групповых чатов.
- Сохранение сообщений в базе данных PostgreSQL.
- Обработка статуса "прочитано".
- REST API для получения истории сообщений.
- Авторизация через JWT.

## Технические требования

- FastAPI для реализации REST API и WebSocket.
- Асинхронная работа через asyncio.
- PostgreSQL в качестве основной базы данных.
- SQLAlchemy для взаимодействия с базой данных.
- Контейнеризация с использованием Docker и Docker Compose.
- Автоматическая документация Swagger / OpenAPI.
- Юнит-тесты с использованием Pytest.

## Запуск проекта

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Rhae9ar/windi-chat.git
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv .venv
    source .venv/bin/activate # Linux/macOS
    .venv\Scripts\activate # Windows
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите Docker Compose:

    ```bash
    docker-compose up --build
    ```

5. Откройте Swagger UI в браузере: `http://localhost:8000/docs`

## Примеры API-запросов

- Получение истории сообщений:

    ```http
    GET /history/{chat_id}?limit=10&offset=0
    ```

- Авторизация и получение токена:

    ```http
    POST /token
    ```

    В теле запроса передать `username` и `password`.

## Создание тестовых данных

Вы можете использовать Swagger UI для создания тестовых пользователей и чатов.

## Юнит-тесты

Для запуска юнит-тестов выполните команду:

    ```bash
    pytest
    ```

## Дополнительно

- Реализована авторизация через JWT.
- Добавлена обработка ошибок и логирование.
- Написаны юнит-тесты с использованием Pytest.

## Конфигурация

Файл `.env` используется для хранения переменных окружения, таких как URL базы данных и секретный ключ JWT. Пример файла `.env`:

    ```env
    SQLALCHEMY_DATABASE_URL=postgresql://user:password@postgres:5432/windi_chat
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    LOG_LEVEL=DEBUG
    ```

Обязательно замените `your_secret_key` на ваш собственный секретный ключ.

## Docker

Для сборки и запуска проекта с помощью Docker выполните:

    ```bash
    docker-compose up --build
    ```

Это запустит контейнеры для приложения и базы данных.

