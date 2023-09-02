# Unit-28
В данном репозитории представлены работы, связанные с модулем 28.

Техники тест дизайна использованные в данном модуле:
1) Эквивалентное разбиение: различные варианты ввода данных для авторизации (корректные, некорректные, пустые) позволяют проверить, как система обрабатывает разные классы входных данных.
2) Граничные значения: тесты с использованием граничных значений (короткие пароли, длинные пароли, неверные номера телефонов) проверяют, как система ведет себя на грани допустимых значений.
3) Позитивное и негативное тестирование: позитивные сценарии (успешная авторизация, регистрация) и негативные сценарии (неверные данные, ошибки валидации) обеспечивают полное покрытие возможных исходов.
4) Комбинационное тестирование: комбинации различных вариантов ввода (номер телефона и пароль, электронная почта и пароль и т.д.) проверяют, как система работает с разными сочетаниями данных.
5) Тестирование переходов: проверка переходов по разным ссылкам и кнопкам, а также корректность переходов между страницами.
6) Тестирование граничных состояний: тесты с неверными данными для восстановления пароля и регистрации помогают проверить, как система обрабатывает необычные ситуации.
7) Параллельное тестирование разных видов авторизации: разные способы авторизации (телефон/почта, логин, лицевой счет) проверяются отдельно, чтобы убедиться, что каждый из них функционирует корректно.
8) Тестирование выхода из аккаунта: проверяет, что пользовательские сессии завершаются корректно.

Мной были использованы данные техники, в связи с тем, что они максимально удобны, просты и затрагивают максимальный функционал заданной страницы для тестирования. 

В автотестах необходимо заменить вводные данные, такие как пароль, логин, мобильный телефон и т.д. на актуальные данные. 
