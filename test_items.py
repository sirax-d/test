import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('browser_language')
class Test_pytest:
    def test_button_cart(self, browser, request):
        language = request.config.getoption("--language")
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/" # Получаем экземпляр браузера из фикстуры
        browser.get(link)
        time.sleep(30)
        button_re = browser.find_elements(By.TAG_NAME, "button")
        assert button_re, "Отсутствует кнопка"

