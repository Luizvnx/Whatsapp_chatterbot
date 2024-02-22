from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
<<<<<<< HEAD
from usecase.obter_contato import obter_contato
from dao.Dao import Dao
import edita_codigo_api
=======
from usecase.responder_clientes import response
import Bot_whatsapp.source.edita_codigo_api as edita_codigo_api
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
import session

def buscar():

    try:
        bolinhas = WebDriverWait(session.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, edita_codigo_api.bolinha_notificacao))
        )

        clica_bolinha = bolinhas[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(session.driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
          
        todas_as_msg = WebDriverWait(session.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, edita_codigo_api.msg_cliente))
        )

        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print("Mensagem: ", msg)
        if msg is not None and msg !="":
            contato = obter_contato()
            Dao.verificar_contato(contato)
            
    except Exception as e:
        print(f"AGUARDANDO NOVAS MENSAGENS")
        return None
