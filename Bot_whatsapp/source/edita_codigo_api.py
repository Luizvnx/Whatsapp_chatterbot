import time
import requests

agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/xgLNUFtZsAbhZZaxkRh5ofM6Z0YIXwwv" ,  headers=agent)
time.sleep(1)

api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()
view = '//*[@id="app"]/div/div[2]/div[4]/div'