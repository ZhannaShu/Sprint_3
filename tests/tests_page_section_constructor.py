# раздел конструктор

from selenium.webdriver.common.by import By

class TestSectionConstructor:
    def test_go_to_the_buns_section(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()
        name_buns = driver.find_element(By.XPATH, "//h2[contains(text(),'Булки')]").text
        assert name_buns == 'Булки'

    def test_go_to_sauces(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        name_sauces = driver.find_element(By.XPATH, "//h2[contains(text(),'Соусы')]").text
        assert name_sauces == 'Соусы'

    def test_go_to_stuffing(self, driver):
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        name_stuffing = driver.find_element(By.XPATH, "//h2[contains(text(),'Начинки')]").text
        assert name_stuffing == 'Начинки'





