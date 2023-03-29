import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def login(driver):
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()    # клик по кнопке Войти в аккаунт на главной странице
    WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'Войти')]")))  # ожидание кнопки Войти в форме авторизации
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys('Zanna_Shuvalova_8777@yandex.ru')
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
    #driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
    return driver

    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def login_reg(driver):
    name = 'Zanna'
    email = 'Zanna_Shuvalova_8777@yandex.ru'
    password = '123456'
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()  # клик по кнопке Войти в аккаунт на главной стр.
    driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
    driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(name)  # ввести имя
    driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(email)  # ввести Email
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)  # ввести пароль
    driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()  # клик по кнопке Зарегистри
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))  # ожидание формы входа
    return driver

    yield browser
    browser.quit()

#@pytest.fixture(scope='function')
#def

