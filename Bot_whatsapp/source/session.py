import os
<<<<<<< HEAD
import edita_codigo_api
=======
import Bot_whatsapp.source.edita_codigo_api as edita_codigo_api
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from usecase.driver_init import driver

dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/session_token")
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')

def iniciar_sessao(sessao_ativa_callback):
    try:
        print("Iniciando sessão...")
<<<<<<< HEAD
        WebDriverWait(driver, 90).until(
=======
        WebDriverWait(driver, 30).until(
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
            EC.presence_of_all_elements_located((By.XPATH, edita_codigo_api.view))
        )
        print("Verificando sessão...")
        sessao_ativa_callback()

    except Exception as e:
        print(f"Ocorreu um erro ao executar 'session.py': {e}")
<<<<<<< HEAD
=======

def sessao_ativa():
    try:
        print("Verificando sessão...")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, edita_codigo_api.view))
        )
        print("Sessão ativa.")
        return True

    except Exception as e:
        print(f"Erro ao verificar sessão - {e}")
        return False
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
