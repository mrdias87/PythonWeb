from src.model.screen_definitions.elementos_site_seleciona_produto import Elementos_Seleciona_Produto


class Acoes_Seleciona_Produto(Elementos_Seleciona_Produto):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_seleciona_produto(self):
        self.element_lista_produto.click()
