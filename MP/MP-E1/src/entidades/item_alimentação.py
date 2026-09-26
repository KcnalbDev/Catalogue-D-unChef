
itens_alimentação = []

def get_itens_alimentação(): return itens_alimentação

def inserir_item_alimentação(item_alimentação): itens_alimentação.append(item_alimentação)

class ItemAlimentação:

    def __init__(self, nome, preço, avaliação, nível_popularidade):
        self.nome = nome
        self.preço = preço
        self.avaliação = avaliação
        self.nível_popularidade = nível_popularidade

    def __str__(self):
        avaliação_str = self.avaliação if self.avaliação in ('ruim', 'médio', 'bom', 'ótimo')  else ' '
        formato = '{:<31} {:<10} {:<8} {:<10}'
        item_alimentação_formatado = formato.format(self.nome, 'R$' + f'{self.preço:.2f}', avaliação_str, str(self.nível_popularidade))
        return item_alimentação_formatado