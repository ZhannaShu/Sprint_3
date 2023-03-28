from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

class TestRegistration:
    def test_reg(self, driver):
        name = 'Zanna'
        email = 'Zanna_Shuvalova_8777@yandex.ru'
        password = '123456'
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()    # клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(name)    # ввести имя
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(email)   # ввести Email
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)  # ввести пароль
        driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()# клик по кнопке Зарегистри

        #reg = driver.find_element(By.XPATH, "//p[contains(text(),'Такой пользователь уже существует")

        #reg = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[1]/div/div/input"))).get_attribute('value')  # получим значение value
        #assert reg == name

     #  проверка ошибки для некорректного пароля
    def test_error_reg(self, driver):
        name = 'Zanna'
        email = 'Zanna_Shuvalova_8777@yandex.ru'
        password = '12345'
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()    # клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(name)    # ввести имя
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(email)   # ввести Email
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)  # ввести пароль
        driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()
        
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//fieldset[3]/div/p")))
        reg_error = driver.find_element(By.XPATH, "//fieldset[3]/div/p").text()
        assert reg_error == 'Некорректный пароль'



time.sleep(5)
