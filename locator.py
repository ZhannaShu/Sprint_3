from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestData:
    url = 'https://stellarburgers.nomoreparties.site/'
    valid_email = 'Zanna_Shuvalova_8777@yandex.ru'
    valid_password = '123456'
    name = 'Zanna'
    invalid_password = '12345'


    loc_log = "button_button__33qZ0"  # локатор элемента кнопки "Войти в аккаунт" на главной странице

    # = ".//div[class='input pr-6 pl-6 input_type_text input_size_default']/input[name='name']")  # локатор поля Email
