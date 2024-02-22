from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from usecase.obter_contato import obter_contato
from usecase.fechar_contato import fechar_contato
from services.BotService import BotService
from dao.Dao import Dao

_dao = Dao()
user = 'luiz@gmail.com'#NÃO SEI ONDE ESTA MERDA VAI FICAR!!!!!
_botService = BotService()

def response_client(data, contato):
        
        if 'total' in data and data['total'] != '0':
                historico = _dao.ultima_conversa(contato)
                return historico if historico else 'Histórico não encontrado'
        else:
                _dao.inserir_contato(contato, user)

fechar_contato.close()


