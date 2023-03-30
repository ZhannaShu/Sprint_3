#  проверить переход в личный кабинет

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestPersonalAccount:
    def test_go_to_personal_account(self, personal_account):   # переход по клику на Личный кабинет
        driver = personal_account
        driver.find_element(By.XPATH,
                            "//p[contains(text(),'Личный Кабинет')]").click()  # клик по кнопке Личный кабинет
        personal_profile = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']"))).text  # получили текст элемента Профиль
        assert personal_profile == 'Профиль'


