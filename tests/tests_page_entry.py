#  проверка входа

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator


class TestAccountLogin:
    def test_login_the_Login_button_on_the_main_page(self, login):  # вход по кнопке Войти в форме авторизации из главной страницы Войти в аккаунт
        driver = login
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locator.BUTTON_COME_INTO)).click()     # клик по кнопке Войти в форме авторизации
        button_text = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locator.CHECKOUT)).text  # получить текст кнопки Оформить заказ
        assert button_text == 'Оформить заказ'

    def test_login_Personal_account(self, personal_account):    # вход по кнопке «Личный кабинет»
        driver = personal_account
        driver.find_element(*Locator.BUTTON_COME_INTO).click()  # клик по кнопке Войти в форме авторизации
        text_button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locator.CHECKOUT))).text  # ожидание кнопки Оформить заказ и получить текст
        assert text_button == 'Оформить заказ'


    def test_login_through_the_button_in_the_registration_form(self, login_reg):  # вход через кнопку в форме регистрации
        driver = login_reg
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locator.BUTTON_COME_INTO)).click()  # клик по кнопке Войти в форме авторизации
        button_text = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locator.CHECKOUT)).text   # получить текст кнопки Оформить заказ
        assert button_text == 'Оформить заказ'


    def test_login_through_the_button_in_the_password_recovery_form(self, login_restore_password):   #  войти через кнопку в форме восстановления пароля.
        driver = login_restore_password
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(Locator.BUTTON_COME_INTO)).click()   # клик по кнопке Войти в форме авторизации
        button_text = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locator.CHECKOUT)).text    # получить текст кнопки Оформить заказ
        assert button_text == 'Оформить заказ'




