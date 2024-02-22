from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from usecase.obter_contato import obter_contato
from usecase.fechar_contato import fechar_contato
from services.BotService import BotService
<<<<<<< HEAD
from dao.Dao import Dao
=======
import Bot_whatsapp.source.edita_codigo_api as edita_codigo_api
import session
from dto import DTO
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6

_dao = Dao()
user = 'luiz@gmail.com'#NÃO SEI ONDE ESTA MERDA VAI FICAR!!!!!
_botService = BotService()

def response_client(data, contato):
        
        if 'total' in data and data['total'] != '0':
                historico = _dao.ultima_conversa(contato)
                return historico if historico else 'Histórico não encontrado'
        else:
                _dao.inserir_contato(contato, user)

<<<<<<< HEAD
fechar_contato.close()
=======
    contato = obter_contato.get_nome()
 
    if contato is not None:
        try:
            campo_de_texto = session.driver.find_element(By.XPATH,edita_codigo_api.caixa_msg)
            campo_de_texto.click()
            campo_de_texto.send_keys(_botService.iniciar_dialogo(), Keys.ENTER)
            fechar_contato.close()
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6


