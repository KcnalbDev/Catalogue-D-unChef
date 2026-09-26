itens_alimentação = {}

def get_itens_alimentação(): return itens_alimentação

def inserir_item_alimentação(item_alimentação):
    nome_item = item_alimentação.nome
    if nome_item not in itens_alimentação.keys(): itens_alimentação[nome_item] = item_alimentação
    else: print('Item ' + nome_item + ' já tem cadastro')

class ItemAlimentação:
    def __init__(self, nome, preço, avaliação, nível_popularidade):
        self.nome = nome
        self.preço = preço
        self.avaliação = avaliação if avaliação in ('ruim', 'médio', 'bom', 'ótimo') else 'indefinida'
        self.nível_popularidade = nível_popularidade

    def __str__(self):
        formato = '{:<31} {:<10} {:<8} {:<10}'
        item_formatado = formato.format(self.nome, 'R$' + f'{self.preço:.2f}',
                                        self.avaliação, str(self.nível_popularidade))
        return item_formatado