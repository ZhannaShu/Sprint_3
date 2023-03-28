import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")

    browser = webdriver.Chrome(options=options, executable_path="./chromedriver")
    browser.get(url)

    yield browser
    browser.quit()









#driver.get("https://stellarburgers.nomoreparties.site/")  # открыть страницу

#Zanna_Shuvalova_8777@yandex.ru  #  Email

