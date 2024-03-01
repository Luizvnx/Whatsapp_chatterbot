import session
import edita_codigo_api
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from usecase.fechar_contato.fechar_contato import close
from dao.dao import Dao


user = 'luiz@gmail.com'#NÃO SEI ONDE ESTA MERDA VAI FICAR!!!!!
dao = Dao(base_url="http://localhost/BOT_WHATSAPP/index.php?", headers={"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})

def response_client(data, contato):
        
        if 'total' in data and data['total'] != '0':
                historico = dao.ultima_conversa(contato)

                return historico if historico else 'Histórico não encontrado'
        else:
                todas_as_msg = WebDriverWait(session.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, edita_codigo_api.msg_cliente))
                )

                todas_as_msg_texto = [e.text for e in todas_as_msg]
                msg = todas_as_msg_texto[-1]
                dao.inserir_contato(contato, msg)

close()


