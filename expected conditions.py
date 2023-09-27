from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element(By.ID, 'book').click()
    browser.execute_script("window.scrollBy(0, 200);")
    
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button.click()
		

finally:
    time.sleep(15)
    browser.quit()
