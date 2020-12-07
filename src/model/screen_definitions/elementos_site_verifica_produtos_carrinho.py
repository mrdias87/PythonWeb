from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Produtos_Carrinho:

    def __init__(self, driver):
        self.driver = driver
        self.textviewer_nome_produto = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Ração Royal Canin 15kg Maxi Junior Cães '
                                                      'Filhotes de Raças Grandes - 1 Unidade")]')))
        self.textview_nome_fornecedor = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[contains(text(),"Ração Royal Canin 15kg Maxi Junior Cães '
                                                      'Filhotes de Raças Grandes - 1 Unidade")]')))
        self.textviewer_preco_produto = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'right')))
        

