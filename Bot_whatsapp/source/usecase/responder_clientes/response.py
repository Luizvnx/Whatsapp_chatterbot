from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from usecase.obter_contato import obter_contato
from usecase.fechar_contato import fechar_contato
import api
import session
from dto import DTO

user = 'luiz@gmail.com' #NÃO SEI ONDE ESTA MERDA VAI FICAR!!!!!

def response_client(msg):

    contato = obter_contato.get_nome()
    _dto = DTO(contato=contato, user=user)
    
    resposta = _dto.get_response(contato, user)
    if contato is not None and msg is not None:
        try:
            campo_de_texto = session.driver.find_element(By.XPATH,api.caixa_msg)
            campo_de_texto.click()
            campo_de_texto.send_keys(resposta, Keys.ENTER)
            fechar_contato.close()

        except Exception as e:
            print(f"Erro ao responder ao cliente: {e}")
    else: 
        print("nome null")