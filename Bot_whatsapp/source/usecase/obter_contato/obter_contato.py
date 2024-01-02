import session
import time
import api
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def get_nome():
    try:
        contato =  session.driver.find_element(By.XPATH, api.contato_cliente)
        contato_final = contato.text
        print("Contato: ", contato_final)
        time.sleep(1)
        return contato_final
    
    except NoSuchElementException:
        try:
            contato =  session.driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
            nome_grupo = contato.text
            print("Grupo: ", nome_grupo)
            time.sleep(1)
            return None #SO PRA VERIFICAR SE CONTINUA PEGANDO O NOME, MAS N RESPONDE GRUPO!

        except Exception as e:
            print(f"Erro ao obter nome do contato")
            return None
        
