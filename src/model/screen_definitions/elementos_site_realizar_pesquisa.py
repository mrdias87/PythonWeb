from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Elementos_Realizar_Pesquisa:

    def __init__(self, driver):
        self.driver = driver
        self.edit_text_search = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                                                       'inputPesquisa')))
        self.button_search = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                                                    'button-search')))
