from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import session

def close():
    try:
        webdriver.ActionChains(session.driver).send_keys(Keys.ESCAPE).perform()
    except Exception as e:
        print(f"Erro ao fechar o contato: {e}")
