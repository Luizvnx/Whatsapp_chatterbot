from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from usecase.responder_clientes import response
import traceback
import api
import session

def buscar():

    try:
        bolinhas = WebDriverWait(session.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, api.bolinha_notificacao))
        )

        clica_bolinha = bolinhas[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(session.driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
          
        todas_as_msg = WebDriverWait(session.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, api.msg_cliente))
        )

        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print("Mensagem: ", msg)
        if msg != "":
            response.response_client(msg)
        return msg

    except IndexError as e:
        print(f"Índice inválido: {e}")
        return None
    
    except Exception as e:
        print(f"Erro ao obter mensagens não lidas: {e}")
        traceback.print_exc()
        return None
