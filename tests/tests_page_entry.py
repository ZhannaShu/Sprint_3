#  проверка входа
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAccountLogin:
    def test_login_the_Login_button_on_the_main_page(self, login):  # вход по кнопке Войти в форме авторизации из главной страницы Войти в аккаунт
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,
                            "//button[contains(text(),'Войти')]"))).click()  # клик по кнопке Войти в форме авторизации

        # butoon_text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
        # print(butoon_text)
        #button_text = driver.find_element((By.XPATH, "//button[text()='Оформить заказ']"))).text
        #assert
        # assert butoon_text == 'Оформить заказ'

        # WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")))

        # WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//nav/a/p"))) # ожидание элемента Личный Кабинет

        # driver.find_element(By.XPATH, "//nav/a/p").click()  # клик по кнопке Личный Кабинет
        # WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//li[2]//input[value='zanna_shuvalova_8777@yandex.ru']")))

    # ожидание появления кнопки Войти в аккаунт
    # WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0")))

    # ожидание появления поля Email
    # WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//div[class='input pr-6 pl-6 input_type_text input_size_default']/input[name='name']")))

    def test_login_through_button_personal_account(self, login):  # вход через кнопку Личный кабинет
        driver = login
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//nav/a/p")))  # ожидание элемента Личный Кабинет



    def test_login_through_the_button_in_the_registration_form(self, login_reg, login):  # вход через кнопку в форме регистрации




    def test_login_through_the_button_in_the_password_recovery_form(self, login):   #  войти через кнопку в форме восстановления пароля.