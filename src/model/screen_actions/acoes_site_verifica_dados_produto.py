import re
from src.model.screen_definitions.elementos_site_verifica_dados_produto import Elementos_Verifica_Dados_Produto


class Acoes_Verifica_Dados_Produto(Elementos_Verifica_Dados_Produto):

    def __init__(self, driver):
        super().__init__(driver)

    def verificar_texto_nome_produto(self):
        result = self.text_nome_produto.text
        return result

    def verificar_texto_nome_fornecedor(self):
        texto = self.text_nome_fornecedor.text
        nome = re.findall('\\bRoyal Canin\\b', texto, re.IGNORECASE)
        result = nome[0]
        return result

    def verificar_texto_valor_produto(self):
        result = self.text_preco_produto.text
        return result

    def verificar_texto_valor_assinante(self):
        result = self.text_preco_assinante.text
        return result

    def clicar_adicionar_ao_carrinho(self):
        self.button_add_to_cart.click()

