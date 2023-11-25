import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


# Xpaths de los campos del formulario que debemos llenar
XPATHS_CAMPOS = (
    '//input[@ng-reflect-name="labelFirstName"]',    # First Name
    '//input[@ng-reflect-name="labelLastName"]',     # Last Name
    '//input[@ng-reflect-name="labelCompanyName"]',  # Company Name
    '//input[@ng-reflect-name="labelRole"]',         # Role in Company
    '//input[@ng-reflect-name="labelAddress"]',      # Addres
    '//input[@ng-reflect-name="labelEmail"]',        # Email
    '//input[@ng-reflect-name="labelPhone"]'         # Phone Number
)
# Xpath para continuar con el siguiente formulario
BOTON_SUBMIT = '//input[@value="Submit"]'
# Xpath del botón de descarga del archivo
BOTON_DOWNLOAD = '//a[@href="./assets/downloadFiles/challenge.xlsx"]'
# Xpath del botón que inicia el reto
BOTON_START = '//button[text()="Start"]'
# Xpath del mensaje final del reto
XPATH_MENSAJE = '//div[@class="message2"]'


# -------- ABRIR NAVEGADOR --------
driver = webdriver.Chrome()
driver.maximize_window()

# -------- NAVEGAR HASTA EL SITIO WEB --------

driver.get('https://rpachallenge.com/')

# -------- DESCARGAR EL EXCEL --------

driver.find_element(By.XPATH, BOTON_DOWNLOAD).click()

# -------- ABRIR EXCEL --------

pandas = pd.read_excel(os.getcwd() + '/challenge.xlsx')

# -------- INICIAR EL FORMULARIO --------
startButton = driver.find_element(By.XPATH, BOTON_START)
input(BOTON_START).click()

# -------- AVANZAR AL SIGUIENTE REGISTRO --------


# -------- OBTENER REGISTROS --------


# -------- INGRESAR DATOS EN LOS CAMPOS DE TEXTO --------


# -------- ENVIAR LOS DATOS INGRESADOS --------


# -------- EXTRAER RESULTADO --------


# -------- IMPRIMIR RESULTADO --------


# -------- CERRAR NAVEGADOR --------
