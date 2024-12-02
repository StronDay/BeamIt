auth_service = container "Auth" {
    description "Обеспечивает регистрацию, вход, выход и управление токенами для пользователей"
    technology "Flask/Python"

    auth_router = component "Router" {
        description "Выполняет маршрутизацию к соответствующим контроллерам."
        technology "Flask/Python"
    }

    auth_controller = component "Auth controller" {
        description "Обработка запросов Авторизации/Аутентификации."
        technology "Flask/Python"
    }

    token_controller = component "Token controller" {
        description "Обработка запросов токена."
        technology "Flask/Python"
    }

    token_model = component "Token model" {
        description "Структура и обработка запросов к базе данных токена."
        technology "Flask/Python"
    }

    token_util = component "Token util" {
        description "Функционал для работы с JWT-токеном."
        technology "PyJWT/Flask/Python"
    }

    auth_router -> auth_controller "Авторизация/Аутентификация"
    auth_router -> token_controller "Управление токеном"

    token_controller -> token_util "Использует"
    auth_controller -> token_util "Использует"

    token_util -> token_model "Получает/Записывает данные"
}