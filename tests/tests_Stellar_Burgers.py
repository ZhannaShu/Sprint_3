from selenium.webdriver.common.by import By
class TestStellarBurgers:
    def test_registration(self, driver):
        name = 'Zanna'
        email = 'Zanna_Shuvalova_8777@yandex.ru'
        password = '123456'
        driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()    # клик по кнопке Войти в аккаунт
        driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()  # клик по Зарегистрироваться
        driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys(name)    # ввести имя
        driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys(email)   # ввести Email
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)  # ввести пароль
        driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()  # клик по кнопке Зарегистри


