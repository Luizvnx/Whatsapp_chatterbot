import requests

class Dao:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def verificar_contato(self, contato):
        try:
            query_params = {'contato': contato, 'type': '1'}
            url = f"{self.base_url}"
            response = requests.get(url, params=query_params)
            response = response.json()
            print ("verificar ctt", response)
            return response

        except Exception as e:
            return f"Erro ao verificar contato: {e}"

    def ultima_conversa(self, contato):
        try:
            query_params = {'contato': contato, 'type': '3'}
            url = f"{self.base_url}"
            response = requests.get(url, params=query_params)
            response = response.json()
            print("historico: ", response)
            return response
        except Exception as e:
            return f"Erro ao obter última conversa: {e}"

    def inserir_contato(self, contato, msg):
        query_params = {'contato': contato, 'msg_sent': msg, 'type': '2'}
        url = f"{self.base_url}"
        response = requests.post(url, params=query_params)
        return response.json()

    def enviar_perguntas(self):
        try:
            url = f"{self.base_url}"
            query_params = {'type': '4'}
            response = requests.get(url, params=query_params)
            return response.json()
        except Exception as e:
            return f"Erro ao obter última conversa: {e}"
        
