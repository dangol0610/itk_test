# itk_test — FastAPI приложение

Проект реализует API для работы с сущностью "Пользователь" с использованием FastAPI, Pydantic и PostgreSQL.  
API поддерживает следующие действия:

- **List** — получить список пользователей с возможностью фильтрации
- **Get** — получить одного пользователя по ID
- **Create** — создать нового пользователя
- **Update** — изменить данные пользователя по ID
- **Delete** — удалить пользователя по ID

Документация Swagger доступна по адресу: `http://localhost:7000/docs`

---

##  Запуск через Docker

1. **Собрать образы и поднять сервисы**:

```cmd
docker compose build
docker compose up
```

2. **Сервер будет доступен по адресу**: `http://localhost:7000`
   Swagger-документация: `http://localhost:7000/docs`

---


##  Примеры запросов к API

**Список пользователей с возможностью фильтрации**:

```http
GET /users?first_name=Иван&age=30
````

Параметры запроса (query parameters) необязательные:

* `first_name` — фильтр по имени
* `last_name` — фильтр по фамилии
* `email` — фильтр по email
* `age` — фильтр по возрасту
* `birth_date` — фильтр по дате рождения (YYYY-MM-DD)

**Получение пользователя по ID**:

```http
GET /users/1
```

**Создание нового пользователя**:

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

**Обновление пользователя по ID**:

Можно передавать только те поля, которые нужно изменить.

```http
PUT /users/update/1
Content-Type: application/json

{
    "age": 31,
    "email": "ivan_new@mail.com"
}
```

**Удаление пользователя по ID**:

```http
DELETE /users/delete/1
```

Все запросы возвращают JSON с результатом операции.
Swagger-документация доступна по адресу: `http://localhost:7000/docs`

---

## Структура проекта

```cmd
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
