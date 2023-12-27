import time
import requests
import api

class DTO:
    
    def __init__(self, msg, contato, user):
       self.msg = msg
       self.contato = contato
       self.user = user

    def get_response(self, msg, contato, user):
        try:
            respose_ws = requests.get('http://localhost/BOT_WHATSAPP/index.php?', params={'msg':msg, 'contato': contato, 'user':user}, headers=api.agent)
            time.sleep(1)
            respose_ws = respose_ws.text
            print(respose_ws)
            return respose_ws
    
        except requests.exceptions.RequestException as req_err:
            print(f"Erro ao fazer a requisição: {req_err}")