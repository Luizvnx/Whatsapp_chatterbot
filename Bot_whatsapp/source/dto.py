import time
import requests
import api

class DTO:
    
    def __init__(self, user):
        self.user = user

    def response(msg, contato, user):
        try:
            respose_ws = requests.get('http://localhost/BOT_WHATSAPP/index.php?', params={'msg':msg, 'contato': contato, 'user':user}, headers=api.agent)
            time.sleep(1)
            respose_ws = respose_ws.text
            print(respose_ws)
            return respose_ws
    
        except Exception as e:
            print(f"Erro ao buscar mensagem {e}")