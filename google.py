from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com/')

textArea = driver.find_element(By.XPATH, '//textarea[@name="q"]')
textArea.clear()
textArea.send_keys('Concierto Karol G' + Keys.ENTER)

time.sleep(4)

driver.close()


