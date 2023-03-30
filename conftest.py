import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestData
import time

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')  # открываем главную страницу
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')  # для теста вход по кнопке «Войти в аккаунт» на главной
def login(driver):
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()  # клик по кнопке Войти в аккаунт
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.valid_email)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(TestData.valid_password)
    return driver


@pytest.fixture(scope='function')   # для теста вход через кнопку Личный кабинет
def personal_account(driver):
    driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()  # клик по кнопке Личный кабинет на главной странице
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.valid_email)
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(TestData.valid_password)  #  ввести пароль
    return driver
    #WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]"))).click()

@pytest.fixture(scope='function')   # фикстура вход через кнопку в форме регистрации
def login_reg(driver):
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()  # клик по кнопке Войти в аккаунт на главной стр.
    driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
    driver.find_element(By.XPATH, "//a[@href='/login']").click()                    # клик по Войти в форме регистрации
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.valid_email)  # ввести Email
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(TestData.valid_password)   # ввести пароль
    return driver


@pytest.fixture(scope='function')    # фикстура для входа по кнопки Восстановление пароля
def login_restore_password(driver):
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()  # клик по кнопке Войти в аккаунт на главной стр.
    driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()  # клик по кнопке Восстановить пароль
    driver.find_element(By.XPATH, "//a[@href='/login']").click()   # клик по кнопке Войти в форме Восстановление пароля
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.valid_email)  # ввести Email
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(TestData.valid_password)   # ввести пароль
    return driver


@pytest.fixture(scope='function')   # фикстура вход в личный кабинет;  # переход в конструктор
def personal_account(driver):
    driver.find_element(By.XPATH,
                        "//p[contains(text(),'Личный Кабинет')]").click()  # клик по кнопке Личный кабинет на главной странице
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.valid_email)     # ввести email
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(TestData.valid_password)  #  ввести пароль
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//button[contains(text(),'Войти')]"))).click()  # клик по кнопке Войти в форме авторизации
    return driver










