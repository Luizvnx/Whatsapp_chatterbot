from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from usecase.obter_contato.obter_contato import get_nome
from dao.dao import Dao
from usecase.responder_clientes.response import response_client
import edita_codigo_api
import session

dao = Dao(base_url="http://localhost/BOT_WHATSAPP/index.php?", headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})

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
        contato = get_nome()
        if contato is not None:
            data = dao.verificar_contato(contato)
            response_client(data, contato)
            
    except Exception as e:
        print(f"AGUARDANDO NOVAS MENSAGENS")
        return None
