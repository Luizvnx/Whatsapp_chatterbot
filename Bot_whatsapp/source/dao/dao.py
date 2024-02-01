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
            data = response.json()
        
            if 'total' in data and data['total'] == '1':
                historico = self.ultima_conversa(contato)
                return historico if historico else 'Histórico não encontrado'
            else:
                return False
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
        url = f"{self.base_url}/inserir_contato"
        data = {'contato': contato, 'user': user}
        response = requests.post(url, data=data)
        return response.json()
    
    def enviar_perguntas(self):
        try:
            url = f"{self.base_url}/perguntas"
            query_params = {'type': '4'}
            response = requests.get(url, params=query_params)
            return response.json()
        except Exception as e:
            return f"Erro ao obter última conversa: {e}"