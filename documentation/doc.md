Ключевые сценарии использования системы:

    1. Пользователь регистрируется в системе.
    2. Пользователь может отправлять и получать приватные (PtP) сообщения с другими пользователями.

Приоритеты нефункциональных требований:

    Требование 1: Безопасность

        Приоритет: Высокий

        Описание: Система должна обеспечивать защиту данных от несанкционированного доступа.
        Контекст: Данное требование ко всей системе, включая основные компоненты и интерфейсы взаимодействия пользователей и системы

        Показатели:

            1. Аутентификация по паролю: все пользователи должны проходить аутентификацию с использованием надежного пароля, который соответствует минимальным требованиям безопасности (длина не менее 8 символов, включение букв, цифр и специальных символов).
            2. Шифрование данных: Передача всех данных должна выполняться через защищенный канал с использованием протокола SSL; данные, хранящиеся на сервере, должны быть зашифрованы с применением алгоритма AES-256.

    Требование 2: Производительность

        Приоритет: Средний

        Описание: Система должна обеспечивать минимальные задержки при выполнении операций и эффективную обработку запросов в условиях нормальной и пиковой нагрузки.
        Контекст: Данное требование применяется в условиях эксплуатации системы в режиме нормальной нагрузки.

        Показатели:

            1. Пропускная способность: Система должна обрабатывать до 500 запросов в секунду в условиях нормальной нагрузки и до 5000 запросов в секунду при пиковой нагрузке.
            2. Время отклика: Время отклика на основные запросы (например, авторизация пользователя, отправка сообщений) не должно превышать 250 мс при обычной нагрузке и 300 мс при пиковой нагрузке.

    Требование 3: Надежность

        Приоритет: Низкий

        Описание: Система должна обеспечивать надежность работы в условиях нормальной эксплуатации, а также должна иметь возможность восстановления после сбоев и аварийных ситуаций.
        Контекст: Данное требование применяется в условиях эксплуатации системы в режиме нормальной нагрузки.

        Показатели:

            1. Система должна быть спроектирована таким образом, чтобы продолжать работать при выходе из строя отдельных компонентов.