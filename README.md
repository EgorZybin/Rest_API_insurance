# Insurance Calculator API

## Описание

API для расчёта стоимости страхования грузов в зависимости от типа груза и объявленной стоимости.

## Технологии

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Docker Compose

## Установка и запуск

1. Клонируйте репозиторий:
```
   git clone https://github.com/your-repo/insurance_calculator.git
   cd insurance_calculator
```

2. Запустите Docker Compose:
```
   docker-compose up --build
```

После успешного запуска, API будет доступно по адресу: http://localhost:8000.

## Документация

Документация API доступна по адресу: http://localhost:8000/docs

# Эндпоинты

- POST /rates/ - добавление нового тарифа
- GET /insurance/{cargo_type}/{value}/{date} - расчёт стоимости страхования