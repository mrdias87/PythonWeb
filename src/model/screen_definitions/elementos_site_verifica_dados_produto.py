from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Elementos_Verifica_Dados_Produto:

    def __init__(self, driver):
        self.driver = driver
        self.text_nome_produto = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/main/div[1]/div[1]/div[1]/div[3]/h1')))
        self.text_nome_fornecedor = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/main/div[1]/div[1]/div[1]/div[3]/h1')))
        self.text_preco_produto = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/main/div[1]/div[1]/div[2]/div[3]/div[1]/div['
                                                      '1]/div[1]/div')))
        self.text_preco_assinante = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/main/div[1]/div[1]/div[2]/div[3]/div['
                                                      '1]/div[2]/div[1]/div[1]/span[1]')))
        self.button_add_to_cart = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'adicionarAoCarrinho')))
