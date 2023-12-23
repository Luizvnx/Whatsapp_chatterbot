import api
import session

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class cliente:
    def __init__(self, nome, mensagem):
        self.nome = nome
        self.mensagem = mensagem

    def mensagens(self):
        todas_as_msg = WebDriverWait(session.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, api.msg_cliente))
        )
        return todas_as_msg

    def ultima_mensagem(self):
        todas_as_msg = self.mensagens()
        todas_as_msg_texto = [e.text for e in todas_as_msg]
        msg = todas_as_msg_texto[-1]
        return msg

