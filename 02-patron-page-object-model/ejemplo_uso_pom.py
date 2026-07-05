from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PageWeather:
 # Define los elementos de la página: cada elemento es una tupla que contiene un localizador
    item = ('localizador')
    main_title = ('localizador')
    site_logo = ('localizador')
    settlement = ('localizador')

    def __init__(self, driver):
                # Inicializando la clase con un controlador de Selenium
        self.driver = driver

    def check_settlement_name(self):
                # Buscando el elemento "main_title", obteniendo su texto y comparándolo con el valor esperado.
        actually_settlement = self.driver.find_element(*self.main_title).text
        expected_settlement = 'localizador'
        assert actually_settlement == expected_settlement

    def select_settlement(self):
                # Haciendo clic en el elemento identificado por "item"
        self.driver.find_element(*self.item).click()

    def set_settlement(self):
                # Agregando el valor de 'location' al elemento identificado por "settlement"
        self.driver.find_element(*self.settlement).send_keys('localizador')

    def wait_for_load_home_page(self):
                # Esperando hasta que "site_logo" sea visible, indicando que la página se ha cargado
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.site_logo))

class TestPageWeather:
    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()
        # Abre la página principal del servicio meteorológico.
        cls.driver.get('URL')
        # Crea un objeto de página
        cls.home_page = PageWeather(cls.driver)

    def test_weather_for_selected_settlement(self):
        # Espera a que se cargue la página
        self.home_page.wait_for_load_home_page()
        # Introduce la ubicación
        self.home_page.set_settlement()
        # selecciona la ubicación requerida de la lista sugerida
        self.home_page.select_settlement()
        # Comprueba el nombre de la ubicación cuando se muestra la meteorología
        self.home_page.check_settlement_name()

    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()