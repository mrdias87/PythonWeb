from src.model.screen_definitions.elementos_site_realizar_pesquisa import Elementos_Realizar_Pesquisa


class Acoes_Realizar_Pesquisa(Elementos_Realizar_Pesquisa):

    def __init__(self, driver):
        super().__init__(driver)

    def escreve_pesquisa_produto(self, texto):
        self.edit_text_search.send_keys(texto)

    def clicar_botao_procura(self):
        self.button_search.click()