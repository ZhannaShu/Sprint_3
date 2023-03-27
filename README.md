Проект автоматизации тестирования сервиса Stellar Burgers
https://stellarburgers.nomoreparties.site/

1. основа для написания автотестов - Selenium
2. В директории tests рассположены файлы с тестами
- tests page registration.py ------------- проверка регистрации
- tests page entry.py -------------------- проверка входа
- tests page go to personal account.py --- переход в личный кабинет
- tests page transition from personal account to the constructor.py --- переход из личного кабинета в конструктор
- tests page logout.py ------------------- выход из аккаунта
- tests page section constructor.py ------ раздел конструктор

3. В файле conftest.py прописаны фикстуры к тестам проекта
4. В файле tests_data.py описание элементов и их локаторы