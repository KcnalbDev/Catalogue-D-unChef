from src.entidades.chef import Chef, inserir_chef, get_chefs
from src.entidades.item_alimentação import ItemAlimentação, inserir_item_alimentação, get_itens_alimentação
from src.entidades.menu import Menu, inserir_menu, get_menus
from src.util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo
from src.util.data import Data

def cadastrar_itens_alimentação():
    inserir_item_alimentação(ItemAlimentação('Lasanha à Bolonhesa', 45.00, 'ótimo', 10))
    inserir_item_alimentação(ItemAlimentação('Fettuccine', 30.00, 'médio', 7))
    inserir_item_alimentação(ItemAlimentação('Canelone de Queijo', 40.00, 'ruim', 6))
    inserir_item_alimentação(ItemAlimentação('Picanha na Chapa', 85.00, 'ótimo', 10))
    inserir_item_alimentação(ItemAlimentação('Filé Mignon ao Molho Madeira', 70.00, 'bom', 8))
    inserir_item_alimentação(ItemAlimentação('Alcatra Acebolada', 55.00, 'bom', 9))
    inserir_item_alimentação(ItemAlimentação('Costela Suína ao Barbecue', 65.00, 'ruim', 6))

def cadastrar_chefs():
    inserir_chef(Chef('Angelina', 15, True, Data(5, 6, 1990)))
    inserir_chef(Chef('Alex Ayala', 11, True, Data(12, 3, 1985)))
    inserir_chef(Chef('Helena Rizzo', 18, True, Data(7, 9, 1978)))
    inserir_chef(Chef('Erick Jacquin', 25, False, Data(2, 11, 1971)))
    inserir_chef(Chef('Albert Landgraf', 12, False, Data(19, 4, 1982)))
    inserir_chef(Chef('Massimo Nakamura', 4, False, Data(28, 8, 1995)))
    inserir_chef(Chef('Ken Holm', 8, False, Data(14, 1, 1988)))

def cadastrar_menus():
    menu = Menu('Menu Especial', 'almoço', 'Helena Rizzo')
    menu.inserir_itens_alimentação(['Costela Suína ao Barbecue', 'Lasanha à Bolonhesa', 'Filé Mignon ao Molho Madeira'])
    inserir_menu(menu)

    menu = Menu('Menu do Dia', 'jantar', 'Erick Jacquin')
    menu.inserir_itens_alimentação(['Filé Mignon ao Molho Madeira', 'Canelone de Queijo', 'Alcatra Acebolada'])
    inserir_menu(menu)

    menu = Menu('Menu Executivo', 'almoço', 'Ken Holm')
    menu.inserir_itens_alimentação(['Canelone de Queijo', 'Picanha na Chapa', 'Fettuccine'])
    inserir_menu(menu)

if __name__ == '__main__':
    print('\nRestaurante com Ítens de Alimentação em um Menu criados por um Chef')
    cadastrar_itens_alimentação()
    imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade', get_itens_alimentação().values())
    cadastrar_chefs()
    imprimir_objetos('Chef : nome, anos de experiência, estrangeiro, data de nascimento', get_chefs().values())
    cadastrar_menus()
    imprimir_objetos('Menu : nome, tipo, chef', get_menus().values())

    for menu in get_menus().values():
        print('\n\n Menu : ' + str(menu))
        itens_menu = menu.itens_alimentação.values()
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade', itens_menu)

        itens_ordenados = ordenar_objetos_por_um_atributo(objetos = itens_menu,
            comparador=lambda item1, item2: item1.nível_popularidade > item2.nível_popularidade)
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade --- ordenado por ordem decrescente de nível de popularidade', itens_ordenados)

        itens_ordenados = ordenar_objetos_por_um_atributo(objetos = itens_menu,
            comparador=lambda item1, item2: item1.preço > item2.preço)
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade --- ordenado por ordem decrescente de preço', itens_ordenados)