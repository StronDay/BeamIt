workspace {
    name "BeamIt Messenger"

    model {
        user = person "Пользователь" {
            description "Использует приложение для общения и управления чатами."
        }

        beamit = softwareSystem "BeamIt" {

            !include client_model.dsl
            !include auth_model.dsl
            !include users_model.dsl

            api_gateway = container "ApiGeteway" {
                description "Распределяет клиентские запросы по сервисам"
                technology "FastApi/Python"
            }

            user -> registration_form "Использует"
            user -> messenger_form "Использует"
            user -> chat_form "Использует"

            registration_form -> api_gateway "Отправляет данные" "HTTPs"
            messenger_form -> api_gateway "Отправляет данные" "HTTPs"
            chat_form -> api_gateway "Отправляет данные" "HTTPs"

            users_data_base = container "Users DB" {
                description "База данных которая хранит данные пользователей"
                technology "PostgreSQL"
            }

            messege_data_base = container "Messege DB" {
                description "База данных которая хранит данные чатов и сообщений"
                technology "PostgreSQL"
            }

            cipher_service = container "Cipher" {
                description "Обеспечивает работу с алгоритмами шифрования"
                technology "Flask/Python"
            }

            messege_service = container "Messege" {
                description "Обеспечивает отправку/чтение сообщений"
                technology "Flask/Python"
            }

            chat_service = container "Chat" {
                description "Обеспечивает управление чатам сервиса"
                technology "Flask/Python"
            }

            api_gateway -> auth_router "Авторизация/Аутентификация/Проверка токена" "HTTPs"
            api_gateway -> users_router "Получение информации о пользователях" "HTTPs"

            api_gateway -> messege_service "Пересылка сообщений" "HTTPs"
            api_gateway -> chat_service "Управлние чатами" "HTTPs"

            messege_service -> cipher_service "Шифрование/Дешифрование сообщений" "HTTPs"
            messege_service -> messege_data_base "Запись/Чтение данных о сообщениях" "SQL"
            chat_service -> messege_data_base "Запись/Чтение данных о чатах" "SQL"

            auth_controller -> users_router "Получение информации о пользователях" "HTTps"
            auth_controller -> cipher_service "Шифрует/Дешифрует необходимые данные"

            user_controller -> cipher_service "Шифрует/Дешифрует необходимые данные"

            token_model -> users_data_base "Запись/Чтение данных о токенах" "SQL"
            users_model -> users_data_base "Запись/Чтение данных о пользователях" "SQL"
        }
    }

    views {
        theme default

        systemContext beamit {
            description "Контекст Мессенджера BeamIt."
            include *
            autolayout lr
        }

        container beamit {
            description "Контекст Мессенджера BeamIt."
            include *
            autolayout lr
        }

        component web_app {
            include *
            autolayout lr
        }

        component auth_service {
            include *
            autolayout lr
        }

        component users_service {
            include *
            autolayout lr
        }

        dynamic web_app {
            description "Последовательность регистрации пользователя"
            autolayout lr

            user -> registration_form "Заполнил данные регистрации"
            registration_form -> api_gateway "POST [/api/registration] Пересылает данные регистрации пользователя по HTTPs"

            api_gateway -> auth_router "POST [auth/registration] Передаёт данные пользователя"
            auth_router -> auth_controller "Передат данные для обработки"

            auth_controller -> cipher_service "Хеширует пароль"
            auth_controller -> users_router "Передаёт данные для создания пользователя"
            
            users_router -> user_controller "Передаёт данные для обработки"
            user_controller -> users_util "Создаёт пользователя"
            users_util -> users_model "Проверяет наличия пользователя в бд и при отсутсвии создаёт"
            users_model -> users_data_base "Добавляет зпись о новом пользователе"

            auth_controller -> token_util "Создаёт access и refresh токены и сохраняет их"
        }
    }


}