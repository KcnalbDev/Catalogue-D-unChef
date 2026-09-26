from src.util.data import Data

chefs = []

def get_chefs(): return chefs

def inserir_chef(chef): chefs.append(chef)

class Chef:

    def __init__(self, nome, anos_experiência, estrangeiro, data_nascimento):
        self.nome = nome
        self.anos_experiência = anos_experiência
        self.estrangeiro = estrangeiro
        self.data_nascimento = data_nascimento

    def __str__(self):
        if self.estrangeiro: estrangeiro_str = 'estrangeiro'
        else: estrangeiro_str = ' '
        formato = '{:<19} {:<5} {:<14} {:<10}'
        chef_formatado = formato.format(self.nome, str(self.anos_experiência), estrangeiro_str, str(self.data_nascimento))
        return chef_formatado
