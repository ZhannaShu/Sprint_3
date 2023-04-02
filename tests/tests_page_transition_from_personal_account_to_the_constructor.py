# переход из личного кабинета в конструктор

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator


class TestJumpConstructor:
    def test_transition_by_click_to_the_constructor_from_the_personal_account(self, go_to_personal_account):  # переход по клику на Конструктор в личном кабинете
        driver = go_to_personal_account
        driver.find_element(*Locator.ACCOUNT).click()            # клик по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.PROF))  # ожидание элемента Профиль
        driver.find_element(*Locator.CONSTRUCTOR).click()        # клик по кнопке Конструктор в личном кабинете
        personal_account_costructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.ELEMENT_BURGER)).text  # получить текст элемента Соберите бургер в Конструкторе
        assert personal_account_costructor == 'Соберите бургер'


    def test_transition_by_click_to_the_constructor_from_the_logo_stellar_burgers(self, go_to_personal_account):  # переход по клику на логотип Stellar Burgers из личного кабинета
        driver = go_to_personal_account
        driver.find_element(*Locator.ACCOUNT).click()               # клик по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.PROF))  # ожидание элемента Профиль
        driver.find_element(*Locator.BUTTON_STELLAR_BUR).click()    # клик по элементу stellar burgers в Личном кабинете
        personal_account_costructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.ELEMENT_BURGER)).text
        assert personal_account_costructor == 'Соберите бургер'


