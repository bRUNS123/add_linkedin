import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
import os
import sys
import glob
import shutil

# Variables
Chrome_Dir = ".\chromedriver.exe"
Url = "https://www.linkedin.com/mynetwork/"



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


# Iniciar Chrome y grabar perfil
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
s = Service(resource_path('./driver/chromedriver.exe'))
op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'], )
op.add_experimental_option("detach", True)
op.add_argument(
    r"user-data-dir={}".format(profile))
driver = webdriver.Chrome(service=s, options=op)
driver.get(Url)
time.sleep(5)

# Wait
wait = WebDriverWait(driver, 7, poll_frequency=1, ignored_exceptions=[
                     ElementNotVisibleException, ElementNotSelectableException])

#Mantener abierto

while True:
    try:
        clickDescarga = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//button[normalize-space()="Connect"]'))).click()
        
        try: 
             clickDescarga = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//button[normalize-space()="Got it"]'))).click()

            
        except:
             pass
        
        if "invitation limit" in driver.page_source.lower():
            print("Se ha detectado 'invitation limit'. Cerrando el driver.")
            driver.quit()
            break



    except TimeoutException:
            print("No se encontró ningún botón 'Connect' o ya no hay más botones.")

            driver.refresh()
            time.sleep(10)
            continue
            # break  # Salir del bucle cuando no se encuentre más botones 'Connect'
    
    

