import requests

class Dao:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def verificar_contato(self, contato):
        try:
<<<<<<< HEAD
            _contato = contato
=======
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
            query_params = {'contato': contato, 'type': '1'}
            url = f"{self.base_url}"
            response = requests.get(url, params=query_params)
            data = response.json()
<<<<<<< HEAD
            #rc.response_client(data, _contato)

=======
        
            if 'total' in data and data['total'] == '1':
                historico = self.ultima_conversa(contato)
                return historico if historico else 'Histórico não encontrado'
            else:
                return False
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
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
<<<<<<< HEAD
        query_params = {'contato': contato, 'type': '2'}
        url = f"{self.base_url}"
        data = {'contato': contato, 'user': user}
        response = requests.post(url, data=data, params=query_params)
        return response.json()

    def enviar_perguntas(self):
        try:
            url = f"{self.base_url}"
=======
        url = f"{self.base_url}/inserir_contato"
        data = {'contato': contato, 'user': user}
        response = requests.post(url, data=data)
        return response.json()
    
    def enviar_perguntas(self):
        try:
            url = f"{self.base_url}/perguntas"
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
            query_params = {'type': '4'}
            response = requests.get(url, params=query_params)
            return response.json()
        except Exception as e:
<<<<<<< HEAD
            return f"Erro ao obter última conversa: {e}"
        
dao = Dao(base_url="http://localhost/BOT_WHATSAPP/index.php?", headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})
=======
            return f"Erro ao obter última conversa: {e}"
>>>>>>> 1d50e3c4a052e2910fbad7a0979a2cbc50506de6
