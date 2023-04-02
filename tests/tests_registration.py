# проверка регистрации

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator
class TestRegistration:
    def test_reg(self, driver):
        driver.find_element(*Locator.BUTTON_SING_ACCOUNT).click()    # клик по кнопке Войти в аккаунт
        driver.find_element(*Locator.REG).click()  # клик по Зарегистрироваться в форме авторизации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.NAME))
        driver.find_element(*Locator.NAME).send_keys(Locator.name)    # ввести имя в форме регистрации
        driver.find_element(*Locator.EMAIL).send_keys(f'{Locator.valid_email}')   # ввести Email в форме регистрации
        driver.find_element(*Locator.PASSWORD).send_keys(Locator.valid_password)  # ввести пароль в форме регистрации
        driver.find_element(*Locator.REG_REG).click() # клик по кнопке Зарегистрироваться в форме регистрации
        reg = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locator. BUTTON_USER_EXISTS))).text
        assert reg == "Такой пользователь уже существует"


     #  проверка ошибки для некорректного пароля
    def test_error_reg(self, driver):
        driver.find_element(*Locator.BUTTON_SING_ACCOUNT).click()    # клик по кнопке Войти в аккаунт
        driver.find_element(*Locator.REG).click()  # клик по Зарегистрироваться в форме авторизации
        driver.find_element(*Locator.NAME).send_keys(Locator.name)    # ввести имя
        driver.find_element(*Locator.EMAIL).send_keys(Locator.valid_email)   # ввести Email
        driver.find_element(*Locator.PASSWORD).send_keys(Locator.invalid_password)  # ввести пароль
        driver.find_element(*Locator.REG_REG).click()  # клик по кнопке Зарегистрироваться в форме регистрации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.REG_ERROR))  # ожидание появления ошибки Некорректный пароль
        reg_error = driver.find_element(*Locator.REG_ERROR).text   # получить текст элемента Некор.пароль
        assert reg_error == 'Некорректный пароль'


