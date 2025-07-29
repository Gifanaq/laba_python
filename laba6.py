import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


list_witl_all_parsed_data = list()

options = Options()
options.headless = True
service = Service("C:/Users/Пользователь/Pictures/chromedriver-win64/chromedriver.exe")  # Укажи свой путь к chromedriver.exe
driver = webdriver.Chrome(service=service, options=options)


URL = "https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki"
driver.get(URL)


wait = WebDriverWait(driver, 30)
time.sleep(10)
products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card__wrapper")))


for product in products:
    try:
        title = product.find_element(By.CLASS_NAME, "product-card__name").text.strip()
    except:
        title = "Название не найдено"

    try:
        price_with_discount = product.find_element(By.CLASS_NAME, "price__lower-price").text.strip()
    except:
        price_with_discount = "Нет скидки"

    try:
        price_without_discount = product.find_element(By.TAG_NAME, "del").text.strip()  # Теперь ищем <del>
    except:
        price_without_discount = "Нет старой цены"

    try:
        delivery_time = product.find_element(By.CLASS_NAME, "btn-text").text.strip()
    except:
        delivery_time = "Сроки доставки не указаны"

    try:
        link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = "Ссылка не найдена"

    dicter = {"Название":title[2:],
              "Цена со скидкой": price_with_discount,
              "Цена без скидки": price_without_discount,
              "Доставка":delivery_time,
              "Ссылка":link,


            }
    list_witl_all_parsed_data.append(dicter)



driver.quit()


with open ('output_file.json','w',encoding='utf-8') as f:
    json.dump(list_witl_all_parsed_data,f, ensure_ascii=False,indent=4)
