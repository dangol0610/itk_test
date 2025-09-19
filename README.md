# itk_test — FastAPI API для пользователей

## Локальный запуск

1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
2. Создайте и настройте файл `.env-non-dev` с параметрами подключения к базе данных PostgreSQL.
3. Запустите сервер:
    ```bash
    uvicorn app.main:app --reload --host 0.0.0.0 --port 7000
    ```
4. API будет доступен по адресу: [`http://localhost:7000`](http://localhost:7000)
   Swagger-документация: [`http://localhost:7000/docs`](http://localhost:7000/docs)

**itk_test** — это проект на FastAPI, реализующий CRUD API для работы с сущностью "Пользователь" с использованием Pydantic и PostgreSQL.

## Возможности API

- Получение списка пользователей с фильтрацией
- Получение пользователя по ID
- Создание пользователя
- Обновление пользователя по ID
- Удаление пользователя по ID

Документация Swagger: [`http://localhost:7000/docs`](http://localhost:7000/docs)

---

## Запуск через Docker

1. Соберите и запустите сервисы:

    ```bash
    docker compose build
    docker compose up
    ```

2. Приложение будет доступно по адресу: [`http://localhost:7000`](http://localhost:7000)

---

## Примеры запросов

**Получить список пользователей с фильтрацией:**

```http
GET /users?first_name=Иван&age=30
```

Параметры фильтрации (необязательные):

- `first_name` — имя
- `last_name` — фамилия
- `email` — email
- `age` — возраст
- `birth_date` — дата рождения (YYYY-MM-DD)

**Получить пользователя по ID:**

```http
GET /users/1
```

**Создать пользователя:**

```http
POST /users/create
Content-Type: application/json

{
  "first_name": "Иван",
  "last_name": "Иванов",
  "email": "ivan@mail.com",
  "age": 30,
  "birth_date": "1993-05-15"
}
```

**Обновить пользователя по ID:**

```http
PUT /users/update/1
Content-Type: application/json

{
  "age": 31,
  "email": "ivan_new@mail.com"
}
```

**Удалить пользователя по ID:**

```http
DELETE /users/delete/1
```

Все ответы возвращаются в формате JSON.

---

## Структура проекта

```text
itk_test/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   └── users/
│       ├── models.py
│       ├── service.py
│       ├── schemas.py
│       └── router.py
├── migrations/
├── itk_test.sh
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env-non-dev
└── README.md
```
