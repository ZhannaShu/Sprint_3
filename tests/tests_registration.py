# проверка регистрации
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import TestData
class TestRegistration:
    def test_reg(self, driver):
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()    # клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.name)    # ввести имя
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(TestData.valid_email)   # ввести Email
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(TestData.valid_password)  # ввести пароль
        driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click() # клик по кнопке Зарегистрироваться
        reg = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[@class='input__error text_type_main-default']"))).text
        assert reg == "Такой пользователь уже существует"

     #  проверка ошибки для некорректного пароля
    def test_error_reg(self, driver):
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()    # клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(TestData.name)    # ввести имя
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(TestData.valid_email)   # ввести Email
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(TestData.invalid_password)  # ввести пароль
        driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//fieldset[3]/div/p")))  # ожидание появления ошибки
        reg_error = driver.find_element(By.XPATH, "//fieldset[3]/div/p").text   # получили текст элемента Некор.пароль
        assert reg_error == 'Некорректный пароль'


