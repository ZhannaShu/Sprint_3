# раздел конструктор

from locator import Locator

class TestSectionConstructor:
    def test_go_to_the_buns_section(self, driver):    # проверяем переход в раздел Булки
        driver.find_element(*Locator.SAUCES).click()  # клик по кнопке Соусы в строке выбора инградиентов
        driver.find_element(*Locator.BUNS).click()    # клик по кнопке Булки в строке выбора инградиентов
        name_buns = driver.find_element(*Locator.BUN_SECTION).get_attribute('class')   # получить значение атрибута class
        assert name_buns == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_go_to_sauces(self, driver):              # проверяем переход в раздел Соусы
        driver.find_element(*Locator.SAUCES).click()  # клик по кнопке Соусы в строке выбора инградиентов
        name_sauces = driver.find_element(*Locator.SAUCES_SECTION).get_attribute('class')   # получить значение атрибута class
        assert name_sauces == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


    def test_go_to_stuffing(self, driver):              # проверяем переход в раздел Начинки
        driver.find_element(*Locator.STUFFING).click()  # клик по кнопке Начинки в строке выбора инградиентов
        name_stuffing = driver.find_element(*Locator.STUFFING_SECTION).get_attribute('class')  # получить значение атрибута class
        assert name_stuffing == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'






