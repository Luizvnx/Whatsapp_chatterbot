from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


def inicializar_driver():
    dir_path = os.getcwd()
    chrome_options2 = Options()
    chrome_options2.add_argument(r"user-data-dir=" + dir_path + "profile/session_token")
    driver = webdriver.Chrome(chrome_options2)
    driver.get('https://web.whatsapp.com/')
    return driver