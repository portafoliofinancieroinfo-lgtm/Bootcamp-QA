import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# iniciar el navegador
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(5)

# Buscar elementos
find_email = driver.find_element(By.ID, "email")
find_password = driver.find_element(By.ID, "password")

# Probar el atributo placeholder para cada elemento
assert find_email.get_attribute("placeholder") == "Correo electrónico", f"Correo esperado: 'Correo electrónico', actual: '{find_email.get_attribute('placeholder')}'"
assert find_password.get_attribute("placeholder") == "Contraseña", f"Contraseña esperada: 'Contraseña', actual: '{find_password.get_attribute('placeholder')}'"

# Cerrar el navegador
driver.quit()
