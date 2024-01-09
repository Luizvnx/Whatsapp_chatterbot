from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from usecase.obter_contato import obter_contato
from usecase.fechar_contato import fechar_contato
from services.BotService import BotService
import api
import session
from dto import DTO

user = 'luiz@gmail.com'#NÃO SEI ONDE ESTA MERDA VAI FICAR!!!!!
_botService = BotService()

def response_client():

    contato = obter_contato.get_nome()
    _dto = DTO(contato, user)
    
    resposta = _dto.get_response(contato, user)
    if contato is not None:
        try:
            campo_de_texto = session.driver.find_element(By.XPATH,api.caixa_msg)
            campo_de_texto.click()
            #campo_de_texto.send_keys(_botService.iniciar_dialogo(), Keys.ENTER)
            campo_de_texto.send_keys(_botService.print_json(), Keys.ENTER)
            fechar_contato.close()

        except Exception as e:
            print(f"Erro ao responder ao cliente: {e}")
            fechar_contato.close()
    else: 
        print("nome null")
        fechar_contato.close()

