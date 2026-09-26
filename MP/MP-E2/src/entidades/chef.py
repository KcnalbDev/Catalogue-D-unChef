chefs = {}

def get_chefs(): return chefs

def inserir_chef(chef):
    nome_chef = chef.nome
    if nome_chef not in chefs.keys(): chefs[nome_chef] = chef
    else: print('Chef ' + nome_chef + ' já tem cadastro')

class Chef:
    def __init__(self, nome, anos_experiência, estrangeiro, data_nascimento):
        self.nome = nome
        self.anos_experiência = anos_experiência
        self.estrangeiro = estrangeiro
        self.data_nascimento = data_nascimento

    def __str__(self):
        if self.estrangeiro: estrangeiro_str = 'estrangeiro'
        else: estrangeiro_str = ' '
        formato = '{:<19} {:<5} {:<13} {:<10}'
        chef_formatado = formato.format(self.nome, str(self.anos_experiência), estrangeiro_str, str(self.data_nascimento))
        return chef_formatado