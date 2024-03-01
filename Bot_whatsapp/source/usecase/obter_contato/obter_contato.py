import session
import time
import edita_codigo_api
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from usecase.fechar_contato.fechar_contato import close

def get_nome():
    try:
        contato = session.driver.find_element(By.XPATH, edita_codigo_api.contato_cliente)
        contato_final = contato.text
        print("Contato:", contato_final)
        time.sleep(1)
        return contato_final
    except NoSuchElementException:
        try:
            contato = session.driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
            nome_grupo = contato.text
            print("Grupo:", nome_grupo)
            time.sleep(1)
            close()
            return None  # Retorna None para indicar que é um grupo
        
        except NoSuchElementException as e:  # Captura apenas a exceção NoSuchElementException
            print("Erro ao obter nome do contato:", e)
            return None
  
