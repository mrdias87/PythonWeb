from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Seleciona_Produto:

    def __init__(self, driver):
        self.driver = driver
        self.element_lista_produto = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
              By.XPATH, '//img[@alt="Ração Royal Canin 15kg Maxi Junior Cães Filhotes de Raças Grandes"]')))
