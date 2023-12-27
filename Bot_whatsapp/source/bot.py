from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from dto import DTO
import api
import session
import time

msg = ''
contato = ' '
user = 'luiz@gmail.com'
_dto = DTO(msg=msg, contato=contato, user=user)


def iniciar_sessao():
    try:
        exec(open('session.py').read())
        pass
    except FileNotFoundError:
        print("O arquivo 'session' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao executar 'session.py': {e}")

#REFACTOR
def obter_nome_do_contato():
    try:
        contato =  session.driver.find_element(By.XPATH, api.contato_cliente)
        contato_final = contato.text
        print("Contato: ", contato_final)
        time.sleep(3)
        return contato_final
    
    except NoSuchElementException:
        try:
            contato =  session.driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
            nome_grupo = contato.text
            print("Grupo: ", nome_grupo)
            time.sleep(3)
            return None #SO PRA VERIFICAR SE CONTINUA PEGANDO O NOME, MAS N RESPONDE GRUPO!

        except Exception as e:
            print(f"Erro ao obter nome do contato")
            return None
        

def obter_mensagens_nao_lidas():
    try:

        bolinhas = WebDriverWait(session.driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, api.bolinha_notificacao))
        )

        clica_bolinha = bolinhas[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(session.driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha, 0, -20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
          
        #REFACTOR
        todas_as_msg = WebDriverWait(session.driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, api.msg_cliente))
        )

        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        print("Mensagem: ", msg)
        return msg

    except Exception as e:
        print(f"Erro ao obter mensagens não lidas: {e}")
        return None
    
    

#REFACTOR
def responder_cliente(msg):

    contato = obter_nome_do_contato()
    
    resposta = _dto.get_response(msg, contato, user)
    if contato is not None and msg is not None:
        try:
            campo_de_texto = session.driver.find_element(By.XPATH,api.caixa_msg)
            campo_de_texto.click()
            campo_de_texto.send_keys(resposta, Keys.ENTER)
            fechar_contato()

        except Exception as e:
            print(f"Erro ao responder ao cliente: {e}")
    else: 
        print("nome null")

def fechar_contato():
    try:
        webdriver.ActionChains(session.driver).send_keys(Keys.ESCAPE).perform()
    except Exception as e:
        print(f"Erro ao fechar o contato: {e}")

def bot():
    while True:
        msg = obter_mensagens_nao_lidas()
        if msg is not None:
            responder_cliente(msg)
        else:
            print('AGUARDANDO NOVAS MENSAGENS')

if __name__ == "__main__":
    iniciar_sessao()
    bot()
