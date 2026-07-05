from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Creación del driver de Chrome
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
wait = WebDriverWait(driver, 10)


# 1. Iniciar sesión
wait.until(expected_conditions.visibility_of_element_located((By.ID, "email"))).send_keys("Tucorreo@gmail.com")
wait.until(expected_conditions.visibility_of_element_located((By.ID, "password"))).send_keys("MiPassword123")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# 2. Agregar una espera explícita para que se cargue la página principal
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__image")))

# 3. Hacer clic en la foto de perfil
driver.find_element(By.CLASS_NAME, "profile__image").click()

# 4. Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
wait.until(expected_conditions.visibility_of_element_located((By.ID, "owner-avatar"))).send_keys(avatar_url)

# 5. Guardar la nueva foto
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Guardar']").click()

# 6. Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
wait.until(expected_conditions.text_to_be_present_in_element_attribute((By.CLASS_NAME, "profile__image"), "style", avatar_url))
style = driver.find_element(By.CLASS_NAME, "profile__image").get_attribute("style")

# 7. Comprobar que style contiene el enlace a la foto de perfil
assert avatar_url in style, f"La URL de la imagen no se encuentra en el atributo de estilo: {style}"

driver.quit()