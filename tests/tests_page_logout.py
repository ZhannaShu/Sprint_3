# выход из аккаунта

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
    def test_exit_by_clicking_the_exit_button_in_account(self, personal_account):   # выход по кнопке «Выйти» в личном кабинете
        driver = personal_account
        driver.find_element(By.XPATH,
                            "//p[contains(text(),'Личный Кабинет')]").click()  # клик по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")))  # ожидание элемента Профиль
        driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()
        exit_logout = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Вход')]"))).text
        assert exit_logout == 'Вход'




