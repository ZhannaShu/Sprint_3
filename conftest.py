import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')  # открываем главную страницу
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')                              # для теста вход по кнопке «Войти в аккаунт» на главной
def login(driver):
    driver.find_element(*Locator.BUTTON_SING_ACCOUNT).click()                          # клик по кнопке Войти в аккаунт
    driver.find_element(*Locator.ELEMENT_EMAIL).send_keys(Locator.valid_email)         # ввести email в форме авторизации
    driver.find_element(*Locator.ELEMENT_PASSWORD).send_keys(Locator.valid_password)   # ввести пароль в форме авторизации
    return driver


@pytest.fixture(scope='function')                                      # фикстура вход через кнопку в форме регистрации
def login_reg(driver):
    driver.find_element(*Locator.BUTTON_SING_ACCOUNT).click()          # клик по кнопке Войти в аккаунт на главной стр.
    driver.find_element(*Locator.REG).click()                          # клик по Зарегистрироваться в форме авторизации
    driver.find_element(*Locator.BUTTON_COME_INTO_REG).click()         # клик по Войти в форме регистрации
    driver.find_element(*Locator.ELEMENT_EMAIL).send_keys(Locator.valid_email)         # ввести Email в форме авторизации
    driver.find_element(*Locator.ELEMENT_PASSWORD).send_keys(Locator.valid_password)   # ввести пароль в форме авторизации
    return driver


@pytest.fixture(scope='function')                                   # фикстура для входа по кнопки Восстановление пароля
def login_restore_password(driver):
    driver.find_element(*Locator.BUTTON_SING_ACCOUNT).click()                          # клик по кнопке Войти в аккаунт на главной стр.
    driver.find_element(*Locator.BUTTON_RESTORE_PASSWORD).click()                      # клик по кнопке Восстановить пароль
    driver.find_element(*Locator.BUTTON_ENTER_PASSWORD_RECOVERY).click()              # клик по кнопке Войти в форме Восстановление пароля
    driver.find_element(*Locator.ELEMENT_EMAIL).send_keys(Locator.valid_email)         # ввести Email в форме авторизации
    driver.find_element(*Locator.ELEMENT_PASSWORD).send_keys(Locator.valid_password)   # ввести пароль в форме авторизации
    return driver

@pytest.fixture(scope='function')                                    # фикстура вход в личный кабинет;  # переход в конструктор
def go_to_personal_account(driver):
    driver.find_element(*Locator.ACCOUNT).click()                                     # клик по кнопке Личный кабинет на главной странице
    driver.find_element(*Locator.ELEMENT_EMAIL).send_keys(Locator.valid_email)        # ввести email в форме авторизации
    driver.find_element(*Locator.ELEMENT_PASSWORD).send_keys(Locator.valid_password)  #  ввести пароль в форме авторизации
    WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locator.BUTTON_COME_INTO)).click()  # клик по кнопке Войти в форме авторизации
    return driver


@pytest.fixture(scope='function')
def personal_account(driver):                                                         # вход по кнопке «Личный кабинет»
    driver.find_element(*Locator.ACCOUNT).click()                                     # Клик по кнопке "Личный кабинет"
    driver.find_element(*Locator.ELEMENT_EMAIL).send_keys(Locator.valid_email)        # ввести Email в форме авторизации
    driver.find_element(*Locator.ELEMENT_PASSWORD).send_keys(Locator.valid_password)  # ввести пароль в форме авторизации
    return driver













