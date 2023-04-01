from selenium.webdriver.common.by import By

class Locator:
    url = 'https://stellarburgers.nomoreparties.site/'
    valid_email = 'zanna_shuvalova_8777@yandex.ru'
    valid_password = '123456'
    name = 'Zanna'
    invalid_password = '12345'

    ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")           # кнопка Личный кабинет на главной странице
    PROF = (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")  # элемент Профиль в личном кабинете
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")          # кнопка Конструктор в личном кабинете
    ELEMENT_BURGER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]")  # элемент Соберите бургер в Конструкторе
    BUTTON_STELLAR_BUR = (By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]")      # кнопка stellar burgers
    BUTTON_SING_ACCOUNT = (By.CLASS_NAME, "button_button__33qZ0")            # кнопка Войти в аккаунт на главной странице
    REG = (By.XPATH, "//p[1]/a[text()='Зарегистрироваться']")                # кнопка Зарегистрироваться в форме авторизации
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")    # кнопка Восстановить пароль в форме авторизации
    BUTTON_ENTER_PASSWORD_RECOVERY = (By.XPATH, "//a[@href='/login']")      # кнопка Войти в форме Восстановления пароля

    NAME = (By.XPATH, "//fieldset[1]//input[1]")                             # поле ввода Имя в форме регистрации
    EMAIL = (By.XPATH, "//fieldset[2]//input[1]")                            # поле ввода email в форме регистрации

    PASSWORD = (By.XPATH, "//input[@type='password']")                    # поле ввода пароль в форме регистрации
    BUTTON_COME_INTO_REG = (By.XPATH, "//a[@href='/login']")              # кнопка Войти в форме регистрации
    REG_REG = (By.XPATH, "//form/button[text()='Зарегистрироваться']")    # кнопка Зарегистрироваться в форме регистрации
    BUTTON_USER_EXISTS = (By.XPATH, "//p[@class='input__error text_type_main-default']")   # кнопка Такой пользователь уже существует
    REG_ERROR = (By.XPATH, "//fieldset[3]/div/p")                         # элемент Некорректный пароль в форме авторизации

    ELEMENT_EMAIL = (By.XPATH, '//fieldset[1]//input[1]')                 # поле ввода Email в форме авторизации
    ELEMENT_PASSWORD = (By.XPATH, '//fieldset[2]//input')                 # поле ввода Пароль в форме авторизации
    BUTTON_COME_INTO = (By.XPATH, "//button[contains(text(),'Войти')]")   # кнопка Войти в форме авторизации
    CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']")            # кнопка Оформить заказ на главной странице

    BUTTON_EXIT = (By.XPATH, "//button[contains(text(),'Выход')]")            # кнопка Выход в личном кабинете
    ELEMENT_ENTRY = (By.XPATH, "//h2[contains(text(),'Вход')]")               # элемент Вход в форме авторизации
    SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")                   # элемент Соусы в строке выбора инградиентов
    BUNS = (By.XPATH, "//span[contains(text(),'Булки')]")                     # элемент Булки в строке выбора инградиентов
    BUN_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]/parent::div")  # элемент Булки после перехода в раздел Булки
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]/parent::div")      # элемент Соусы после перехода в раздел Соусы
    STUFFING = (By.XPATH, "//span[contains(text(),'Начинки')]")               # элемент Начинки в строке выбора инградиентов
    STUFFING_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]/parent::div")   # элемент Начинки после перехода в раздел Начинки






