import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")

#Pausa la ejecución de la página
time.sleep(5)

#Búsqueda de un elemento
driver.find_element(By.XPATH, ".//img")

#Búsqueda de varios elementos
driver.find_element(By.XPATH, ".//input")

#Guardado del elemento buscado
element = driver.find_element(By.XPATH, ".//img")
print(element)

driver.quit()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

driver.find_element(By.CSS_SELECTOR, ".auth-form__title")
driver.quit()