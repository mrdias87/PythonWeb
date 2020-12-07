from src.model.screen_definitions.elementos_site_menu_pesquisa import Elementos_Menu_Pesquisa


class Acoes_Menu_Navegacao(Elementos_Menu_Pesquisa):

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_botao_menu_pesquisa(self):
        self.button_menu_search.click()

