from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import proxys

PATH = "C:\Program Files (x86)\chromedriver.exe" #locate chromedriver file
driver = webdriver.Chrome(PATH)                  #set webdriver as chrome   

link = input("URL: ")

driver.get("https://www.nike.com/ar/sportswear/launch") #main page
snkrPage = driver.find_element_by_class_name("dz_xjzja")
snkrLink = snkrPage.get_attribute("href")
notFormLink = "https://www.nike.com/ar/sportswear/launch/waffle-trainer-2-sp"

def waitPage():
    pass

def login(email, password):
    driver.find_element_by_id("hf_title_signin_membership").click()
    time.sleep(1)
    driver.find_element_by_name("emailAddress").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("password").send_keys(Keys.RETURN)

def getSnkrPage(): #waits for the page to upload new form, when does, enters the form

    while(snkrLink == notFormLink):
        driver.refresh()
        time.sleep(15)

    snkrPage.send_keys(Keys.RETURN)

def dropdownChoice(): #searchs for the best size to choose in dropdown
    size = driver.find_element_by_class_name("erx5h8s0")
    all_options = size.find_elements_by_tag_name("option")
    for option in all_options:
        sizeChoice = option.get_attribute("value")
        
        if sizeChoice == "8":
            option.click()

        if sizeChoice == "8.5":
            option.click()

        if sizeChoice == "9":
            option.click()

        

def fillBox(telefono, dni): #fills the text-boxes of information 
    textboxes = driver.find_elements_by_class_name("e14657ab0")
    x = 1

    for textbox in textboxes:
        
        element = textbox
        if x == 1:
            element.send_keys(telefono)
        else:
            element.send_keys(dni)
        x+=x
        

def checkBox(): #accepts terms and conditions
    check = driver.find_element_by_id("EXPERIENCE_TERMS")
    check.click()

def sendRequest(): #sends form
    send = driver.find_element(By.XPATH, '//button[text()="Registrarse"]')
    send.click()

def newTab(x):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[x])
        driver.get(snkrLink)

def completeForm(): 
    i = 0

    for proxy in proxys.proxys:

        if i != 0:
            newTab(i)
        i+=1
        
        login(proxy.email, proxy.password)

        dropdownChoice()
        fillBox(proxy.telefono, proxy.dni)
        checkBox()
        time.sleep(1)
        sendRequest()

        print(proxy.nombre + " form submitted, DNI: " + str(proxy.dni))
    

#getSnkrPage()

time.sleep(2)

completeForm()

time.sleep(5)


