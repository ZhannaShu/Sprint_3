# переход из личного кабинета в конструктор

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestJumpConstructor:
    def test_transition_by_click_to_the_constructor_from_the_personal_account(self, personal_account):  # переход по клику на Конструктор в личном кабинете
        driver = personal_account
        driver.find_element(By.XPATH,
                            "//p[contains(text(),'Личный Кабинет')]").click()  # клик по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")))  # ожидание элемента Профиль
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        personal_account_costructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))).text
        assert personal_account_costructor == 'Соберите бургер'


    def test_transition_by_click_to_the_constructor_from_the_logo_stellar_burgers(self, personal_account):  # переход по клику на логотип Stellar Burgers из личного кабинета
        driver = personal_account
        driver.find_element(By.XPATH,
                            "//p[contains(text(),'Личный Кабинет')]").click()  # клик по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[@href='/account/profile' and text()='Профиль']")))  # ожидание элемента Профиль
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()
        driver.find_element(By.XPATH, "//header/nav[1]/div[1]/a[1]/*[1]").click()
        personal_account_costructor = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Соберите бургер')]"))).text
        assert personal_account_costructor == 'Соберите бургер'


        time.sleep(5)