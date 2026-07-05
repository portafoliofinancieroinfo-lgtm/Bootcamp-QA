import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# iniciar el navegador
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(5)

# Buscar botón de inicio de sesión
Boton = driver.find_element(By.XPATH, ".//button[@class='auth-form__button']")
Boton.click()
time.sleep(2)

# Cerrar el navegador
driver.quit()