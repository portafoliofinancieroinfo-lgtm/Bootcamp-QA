from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Encontrar el campo del correo electrónico y rellenarlo
driver.find_element(By.ID, "email").send_keys("Tucorreo@gmail.com")
# Encontrar el campo de la Contraseña y rellenarlo
driver.find_element(By.ID, "password").send_keys("MiPassword123")

# Buscar el botón Iniciar sesión y hacer clic en él
driver.find_element(By.CLASS_NAME, "auth-form__button").click()
# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "card__image")))

# Buscar el pie de página
element = driver.find_element(By.TAG_NAME, "footer")
# Desplazar el pie de página a la vista
driver.execute_script("arguments[0].scrollIntoView();", element)
# Comprobar que el pie de página contiene el string 'Around'
assert 'Around' in element.text, f"Error: No se encontró 'Around' en el texto. Texto actual: {element.text}"
print(f"Test passed successfully: Se encontró 'Around' en el footer.")

driver.quit()