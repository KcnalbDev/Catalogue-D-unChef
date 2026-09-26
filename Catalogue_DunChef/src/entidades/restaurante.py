from src.entidades.menu import get_menus
from src.entidades.chef import get_chefs

restaurantes = []

def get_restaurantes(): return restaurantes

def criar_restaurante(local, nome_menu, nome_chef):
    menu = get_menus().get(nome_menu)
    if menu is None:
        print('Menu ' + nome_menu + ' não cadastrado')
        return
    chef = get_chefs().get(nome_chef)
    if chef is None:
        print('Chef ' + nome_chef + ' não cadastrado')
        return
    inserir_restaurante(Restaurante(local, menu, chef))

def inserir_restaurante(restaurante):
    if restaurante not in restaurantes: restaurantes.append(restaurante)
    else: print('Restaurante já cadastrado --- ' + str(restaurante))

class Restaurante:
    def __init__(self, local, menu, chef):
        self.local = local
        self.menu = menu
        self.chef = chef

    def __str__(self):
        formato = '{:<15} {:<17} {:<15}'
        restaurante_formatado = formato.format(self.local, self.menu.nome, self.chef.nome)
        return restaurante_formatado