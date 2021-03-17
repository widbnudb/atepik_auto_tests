from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome() #add your path

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    field_1 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(1) > .form-control")
    field_1.send_keys("First Name")
    field_2 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(2) > .form-control")
    field_2.send_keys("Last Name")
    field_3 = browser.find_element(By.CSS_SELECTOR, ".first_block > .form-group:nth-child(3) > .form-control")
    field_3.send_keys("lzbth@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()