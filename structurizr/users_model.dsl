users_service = container "Users" {
    description "Обеспечивает получение информации о пользователях"
    technology "Flask/Python"

    users_router = component "Router" {
        description "Выполняет маршрутизацию к соответствующим контроллерам."
        technology "Flask/Python"
    }

    user_controller = component "User controller" {
        description "Обработка запросов с пользователями."
        technology "Flask/Python"
    }

    users_model = component "Users model" {
        description "Структура и обработка запросов к базе данных пользователей."
        technology "Flask/Python"
    }

    users_util = component "Users util" {
        description "Функционал для работы с пользователями."
        technology "Flask/Python"
    }

    users_router -> user_controller "Управление пользователями"
    user_controller -> users_util "Использует"
    users_util -> users_model "Получает/Записывает данные"
}