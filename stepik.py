from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import math
import os
import pyperclip




from selenium.webdriver.remote.webelement import WebElement
#driver = webdriver.Chrome(ChromeDriverManager().install())

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/cats.html?"
    browser = webdriver.Chrome()
    browser.get(link)

    #
    # x = browser.find_element()
    # x = int(x)

    # y = calc(x)
    # element_button = browser.find_element(By.TAG_NAME, "submit")
    # driver.execute_script("arguments[0].scrollIntoView();", element_button)
    # radio = browser.find_element(By.CLASS_NAME, "form-check-label")
    # radio.click()
    # radio2 = browser.find_element(By.CLASS_NAME, "form-check-label")
    # radio2.click()
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()


    # x1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    # x2 = browser.find_element(By.XPATH, "//span[@id='num2']")
    # result = int(x1.text) + int(x2.text)

    # select = browser.find_element(By.TAG_NAME, "select")
    # option = browser.find_element(By.XPATH, f"//option[@value='{result}']")
    # option.click()
    # select.click()
    #
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()



    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()
    # x_value: WebElement = browser.find_element(By.XPATH, "//span[@class='input_value']")
    # x_element = browser.find_element(By.XPATH, "//img[@valuex]")


    # # Ваш код, который заполняет обязательные поля
    # input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    # input1.send_keys(y)
    # input_name = browser.find_element(By.XPATH, "//html/body/div/form/div/input[1]")
    # input_name.send_keys("Test")
    # input_lastname = browser.find_element(By.XPATH, "//html/body/div/form/div/input[2]")
    # input_lastname.send_keys("Family")
    # input_email = browser.find_element(By.XPATH, "//html/body/div/form/div/input[3]")
    # input_email.send_keys("email@email.com")
    # input_file = browser.find_element(By.XPATH, '//*[@id="file"]')
    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    # input_file.send_keys(file_path) #добавляем файл
    browser.find_element(By.ID, "button")
    input_submit = browser.find_element(By.TAG_NAME, "button")
    input_submit.click()
    new_window = browser.window_handles[1] #Узнаем id вкладки
    # current_window = browser.current_window_handle
    change_window = browser.switch_to.window(new_window)
    # input_alert = browser.switch_to.alert
    # input_alert.accept()
    input_answer = browser.find_element(By.ID, "answer")
    # time.sleep(1)
    input_value = browser.find_element(By.ID, "input_value")
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

    # # input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    # # input2.send_keys("Petrov")
    # # input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    # # input3.send_keys("asd@asd.cd")
    # # time.sleep(5)
    # # Отправляем заполненную форму
    # button = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    # button.click()
    # button = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    # button.click()
    # time.sleep(1)
    #
    # # находим элемент, содержащий текст
    # # welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # # welcome_text = welcome_text_elt.text
    #
    # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
