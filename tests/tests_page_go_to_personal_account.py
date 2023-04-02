#  проверить переход в личный кабинет
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator import Locator


class TestPersonalAccount:
    def test_go_to_personal_account(self, go_to_personal_account):   # переход по клику на Личный кабинет
        driver = go_to_personal_account
        driver.find_element(*Locator.ACCOUNT).click()  # клик по кнопке Личный кабинет
        personal_profile = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locator.PROF)).text  # получить текст элемента Профиль
        assert personal_profile == 'Профиль'


