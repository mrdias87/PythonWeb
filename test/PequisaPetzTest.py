import unittest
from selenium import webdriver
from src.model.screen_actions.acoes_site_realizar_pesquisa import Acoes_Realizar_Pesquisa
from src.model.screen_actions.acoes_site_verifica_dados_produto import Acoes_Verifica_Dados_Produto
from src.model.screen_actions.acoes_site_seleciona_produto import Acoes_Seleciona_Produto
from src.model.screen_actions.acoes_site_verifica_produtos_carrinho import Acoes_Produtos_Carrinho


class PesquisaPetzTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox(executable_path='D:\\PythonWeb\\venv\\geckodriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.petz.com.br/')

        # Declaração de variáveis com os dados para preenchimento
        self.pesquisa = 'Ração'
        self.nome_produto = 'Ração Royal Canin 15kg Maxi Junior Cães Filhotes de Raças Grandes'
        self.nome_fornecedor = 'Royal Canin'
        self.valor_produto = 'R$ 248,89'
        self.valor_assinante = 'R$ 224,00'

    def test_pesquisa_petz(self):

        try:

            # Preencher o campo pesquisa do site
            preenche_pesquisa_produto = Acoes_Realizar_Pesquisa(self.driver)
            preenche_pesquisa_produto.escreve_pesquisa_produto(self.pesquisa)

            # Clicar na botão de pesquisa da barra de procura
            clica_botao_procura = Acoes_Realizar_Pesquisa(self.driver)
            clica_botao_procura.clicar_botao_procura()

            # Clica no item para validar os dados
            clica_para_selecionar_produto = Acoes_Seleciona_Produto(self.driver)
            clica_para_selecionar_produto.clicar_seleciona_produto()

            # Verifica se os dados que estão na tela estão corretos
            verifica_dados_produto = Acoes_Verifica_Dados_Produto(self.driver)
            self.assertEqual(verifica_dados_produto.verificar_texto_nome_produto(), self.nome_produto)
            self.assertEqual(verifica_dados_produto.verificar_texto_nome_fornecedor(), self.nome_fornecedor)
            self.assertEqual(verifica_dados_produto.verificar_texto_valor_produto(), self.valor_produto)
            self.assertEqual(verifica_dados_produto.verificar_texto_valor_assinante(), self.valor_assinante)

            # Adiciona o produto ao carrinho de compras
            verifica_dados_produto.clicar_adicionar_ao_carrinho()

            # Verfica se os dados estão corretos no carrinho
            verifica_produtos_carrinho = Acoes_Produtos_Carrinho(self.driver)
            self.assertEqual(verifica_produtos_carrinho.verificar_nome_produto_carrinho(), self.nome_produto)
            self.assertEqual(verifica_produtos_carrinho.verificar_nome_fornecedor_carrinho(), self.nome_fornecedor)
            self.assertEqual(verifica_produtos_carrinho.verificar_valor_produto_carrinho(), self.valor_produto)

        except ValueError:
            print(ValueError)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
