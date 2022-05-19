from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import proxys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.nike.com/ar/experiences/details/1628074406175")

submit = driver.find_element_by_tag_name("button")

submit = driver.find_element(By.XPATH, '//button[text()="Unete"]')


time.sleep(5)

driver.close()