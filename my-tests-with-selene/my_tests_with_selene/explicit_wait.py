from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pyperclip

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# price_house = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, (//a[contains(text(), '100$'])))
price_house = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

# if price_house == "$100":
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "book")) #element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.
    )
button.click()
# time.sleep(5)
input_answer = browser.find_element(By.ID, "answer")
    # time.sleep(1)
input_value = browser.find_element(By.XPATH, '//*[@id="input_value"]')
x = input_value.text
y = calc(x)
input_answer.send_keys(y)
button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()
time.sleep(1)
alert = browser.switch_to.alert #Переключаемся на модальное окно
alert_text = alert.text #Объявялем переменную
x = alert_text.split(': ')[-1] # Копируем текст ответа с конца до разделителя
pyperclip.copy(x) #копируем в буфер обмена
print(browser.switch_to.alert.text) #Выводим результат модалки в консоль
# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text
