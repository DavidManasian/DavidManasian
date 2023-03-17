from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(num1,num2):
    return int(num1) + int(num2)
try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    
    num1_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    num2 = num2_element.text
    y = sum(num1,num2)
    browser.find_element(By.CSS_SELECTOR, "[id='dropdown']").click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))
	
    button = browser.find_element(By.XPATH,"//button[@class='btn btn-default']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла