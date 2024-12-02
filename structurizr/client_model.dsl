# Контейнер для фронтенда
web_app = container "Web Application" {
    description "Интерфейс для взаимодействия пользователей с мессенджером."
    technology "HTML/CSS"

    registration_form = component "Форма регистрации/авторизации" {
        description "Позволяет пользователям зарегистрироваться и войти в систему."

        }

    messenger_form = component "Форма мессенджера" {
        description "Отображает сообщения и позволяет их отправлять."
    }

    chat_form = component "Форма чатов" {
        description "Управление групповыми и PtP чатами."
    }
}