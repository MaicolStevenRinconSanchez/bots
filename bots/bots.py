"""
Este script automatiza ciertas acciones en un sitio web utilizando Selenium.

El script carga una página web, espera a que se cargue un elemento específico, hace clic en ese elemento,
luego realiza una serie de clics adicionales en otro elemento de la página.

Requiere la biblioteca Selenium y el controlador de Chrome.
"""
import time
from selenium import webdriver
# Importar los módulos adicionales de Selenium que necesites
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.chrome.service import Service

# Definir la ruta del directorio donde se encuentra el controlador de Chrome
RUTA_DIRECTORIO = "/home/camper/Escritorio/drives/chromedriver"



# Crear un objeto de servicio del controlador de Chrome
servicio = Service(RUTA_DIRECTORIO)

# Inicializar el controlador del navegador pasando el servicio como argumento
driver = webdriver.Chrome(service=servicio)

# Resto del script ...



# Cargar la primera página web
driver.get("https://portales.vanguardia.com/empresasgeneradoras/reconocimientos/votos")

# Esperar hasta que el elemento esté presente en la primera página
elemento_primera_pagina = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Nuevas Empresas"))
)

# Hacer clic en el elemento en la primera página
elemento_primera_pagina.click()

# Esperar a que se cargue la segunda página
WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

# Esperar unos segundos para asegurar que la segunda página se cargue completamente
time.sleep(5)

# Encontrar el elemento por su nombre en la segunda página
elemento_segunda_pagina = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Palonegro Ecoparque S.A.S"))
)

# Definir el número de clics
NUMERO_DE_CLICS = 1000

# Hacer clic en el elemento mil veces en la segunda página
for _ in range(NUMERO_DE_CLICS):
    elemento_segunda_pagina.click()

    # Esperar un breve momento entre cada clic (puedes ajustar este valor según sea necesario)
    time.sleep(0.5)

# Esperar unos segundos antes de cerrar el navegador
time.sleep(5)

# Cerrar el navegador
driver.quit()
