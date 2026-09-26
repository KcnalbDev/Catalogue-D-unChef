from src.entidades.item_alimentação import get_itens_alimentação

menus = {}

def get_menus(): return menus

def inserir_menu(menu):
    nome_menu = menu.nome
    if nome_menu not in menus.keys(): menus[nome_menu] = menu
    else: print('Menu ' + nome_menu + ' já tem cadastro')

class Menu:
    def __init__(self, nome, tipo, armazenamento):
        self.nome = nome if nome in ('Menu do Dia', 'Menu Especial', 'Menu Executivo') else 'Sem Nome'
        self.tipo = tipo if tipo in ('almoço', 'jantar') else 'indefinido'
        self.armazenamento = armazenamento
        self.itens_alimentação = {}

    def __str__(self):
        formato = '{:<16} {:<10} {:<8}'
        menu_formatado = formato.format(self.nome, self.tipo, self.armazenamento)
        return menu_formatado

    def título(self): return self.nome + ' ' + self.tipo.capitalize()

    def inserir_itens_alimentação(self, chaves_itens):
        for nome_item in chaves_itens:
            if nome_item in get_itens_alimentação().keys():
                self.itens_alimentação[nome_item] = get_itens_alimentação()[nome_item]
            else: print('Item ' + nome_item + ' não tem cadastro')