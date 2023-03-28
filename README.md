Проект автоматизации тестирования сервиса Stellar Burgers
https://stellarburgers.nomoreparties.site/

1. основа для написания автотестов - Selenium
2. В директории tests рассположены файлы с тестами
- tests_registration.py ------------- проверка регистрации
- tests_page_entry.py -------------------- проверка входа
- tests_page_go_to_personal_account.py --- переход в личный кабинет
- tests_page_transition_from_personal_account_to_the_constructor.py --- переход из личного кабинета в конструктор
- tests_page_logout.py ------------------- выход из аккаунта
- tests_page_section_constructor.py ------ раздел конструктор

3. В файле conftest.py прописаны фикстуры к тестам проекта
4. В файле locator.py описание элементов и их локаторы