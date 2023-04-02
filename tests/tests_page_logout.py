# выход из аккаунта

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator


class TestLogout:
    def test_exit_by_clicking_the_exit_button_in_account(self, go_to_personal_account):   # выход по кнопке «Выйти» в личном кабинете
        driver = go_to_personal_account
        driver.find_element(*Locator.ACCOUNT).click()  # клик по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.PROF))  # ожидание элемента Профиль
        driver.find_element(*Locator.BUTTON_EXIT).click()   # клик по кнопке Выход в личном кабинете
        exit_logout = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.ELEMENT_ENTRY)).text  # получить текст элемента Вход в форме авторизации
        assert exit_logout == 'Вход'




