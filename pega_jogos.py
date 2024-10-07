from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import dick

def web(games={}):
    # Configura o caminho para o chromedriver
    service = Service('chromedriver.exe')

    # Inicializa o Chrome com o serviço configurado
    driver = webdriver.Chrome(service=service)
    # Acessa o site da Epic Games
    driver.get("https://store.epicgames.com/pt-BR/collection/top-sellers")
    
    # Aguarda até que os elementos com a classe css-2mlzob estejam presentes
    try:
        
        # Define o tempo máximo de espera
        wait = WebDriverWait(driver, 10)  # 10 segundos de timeout
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.css-2mlzob')))

        for element in elements:
            print(element.text)
            games = dick.dicktonary(element.text,games)
            print("")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    finally:
        driver.quit()
        return games

