import requests

class Dao:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def verificar_contato(self, contato):
        try:
            _contato = contato
            query_params = {'contato': contato, 'type': '1'}
            url = f"{self.base_url}"
            response = requests.get(url, params=query_params)
            data = response.json()
            #rc.response_client(data, _contato)

        except Exception as e:
            return f"Erro ao verificar contato: {e}"

    def ultima_conversa(self, contato):
        try:
            query_params = {'contato': contato, 'type': '3'}
            url = f"{self.base_url}"
            response = requests.get(url, params=query_params)
            return response.json()
        except Exception as e:
            return f"Erro ao obter última conversa: {e}"

    def inserir_contato(self, contato, user):
        query_params = {'contato': contato, 'type': '2'}
        url = f"{self.base_url}"
        data = {'contato': contato, 'user': user}
        response = requests.post(url, data=data, params=query_params)
        return response.json()

    def enviar_perguntas(self):
        try:
            url = f"{self.base_url}"
            query_params = {'type': '4'}
            response = requests.get(url, params=query_params)
            return response.json()
        except Exception as e:
            return f"Erro ao obter última conversa: {e}"
        
dao = Dao(base_url="http://localhost/BOT_WHATSAPP/index.php?", headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
