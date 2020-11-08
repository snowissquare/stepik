from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import math

def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

	book = browser.find_element_by_id("book")
	book.click()

	input_value = browser.find_element_by_id("input_value")
	number = input_value.text

	field = browser.find_element_by_id("answer")
	field.send_keys(calc(number))

	button = browser.find_element_by_xpath('//button[@type = "submit"]')
	button.click()

finally:
	time.sleep(20)
	browser.quit()
