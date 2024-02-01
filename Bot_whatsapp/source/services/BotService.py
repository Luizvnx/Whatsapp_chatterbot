import dao
from usecase.obter_contato import obter_contato

_dao = dao
class BotService:

    def __init__(self, contato):
       self.contato = contato 
    
    def existe_registo():
        _dao