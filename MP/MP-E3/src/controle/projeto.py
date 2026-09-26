from src.util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo, ordenar_objetos_por_dois_atributos
from src.util.data import Data
from src.entidades.chef import Chef, inserir_chef, get_chefs
from src.entidades.item_alimentação import ItemAlimentação, inserir_item_alimentação, get_itens_alimentação
from src.entidades.menu import Menu, inserir_menu, get_menus
from src.entidades.restaurante import criar_restaurante, get_restaurantes

def cadastrar_chefs():
    inserir_chef(Chef('Angelina', 15, True, Data(5, 6, 1990)))
    inserir_chef(Chef('Alex Ayala', 11, True, Data(12, 3, 1985)))
    inserir_chef(Chef('Helena Rizzo', 18, True, Data(7, 9, 1978)))
    inserir_chef(Chef('Erick Jacquin', 25, False, Data(2, 11, 1971)))
    inserir_chef(Chef('Albert Landgraf', 12, False, Data(19, 4, 1982)))
    inserir_chef(Chef('Massimo Nakamura', 4, False, Data(28, 8, 1995)))
    inserir_chef(Chef('Ken Holm', 8, False, Data(14, 1, 1988)))

def cadastrar_itens_alimentação():
    inserir_item_alimentação(ItemAlimentação('Lasanha à Bolonhesa', 45.00, 'ótimo', 10))
    inserir_item_alimentação(ItemAlimentação('Fettuccine ao Molho Branco', 38.00, 'médio', 9))
    inserir_item_alimentação(ItemAlimentação('Canelone de Queijo', 35.00, 'médio', 8))
    inserir_item_alimentação(ItemAlimentação('Picanha na Chapa', 85.00, 'ótimo', 10))
    inserir_item_alimentação(ItemAlimentação('Filé Mignon ao Molho Madeira', 70.00, 'bom', 8))
    inserir_item_alimentação(ItemAlimentação('Alcatra Acebolada', 55.00, 'bom', 9))
    inserir_item_alimentação(ItemAlimentação('Costela Suína ao Barbecue', 65.00, 'ruim', 7))

def cadastrar_menus():
    menu = Menu('Menu Especial', 'almoço', 'refrigerado')
    menu.inserir_itens_alimentação(['Canelone de Queijo', 'Lasanha à Bolonhesa', 'Fettuccine ao Molho Branco', 'Filé Mignon ao Molho Madeira',
                                    'Alcatra Acebolada'])
    inserir_menu(menu)

    menu = Menu('Menu do Dia', 'jantar', 'congelado')
    menu.inserir_itens_alimentação(['Canelone de Queijo', 'Lasanha à Bolonhesa', 'Alcatra Acebolada', 'Filé Mignon ao Molho Madeira',
                                    'Picanha na Chapa'])
    inserir_menu(menu)

    menu = Menu('Menu Executivo', 'almoço', 'temperatura ambiente')
    menu.inserir_itens_alimentação(['Canelone de Queijo', 'Picanha na Chapa', 'Fettuccine ao Molho Branco', 'Filé Mignon ao Molho Madeira',
                                    'Costela Suína ao Barbecue'])
    inserir_menu(menu)

def cadastrar_restaurantes():
    criar_restaurante('Dourados', 'Menu Especial', 'Helena Rizzo')
    criar_restaurante('Campo Grande', 'Menu do Dia', 'Erick Jacquin')
    criar_restaurante('São Paulo', 'Menu Executivo', 'Ken Holm')

if __name__ == '__main__':
    print('\nRestaurante com Ítens de Alimentação em um Menu criados por um Chef')
    cadastrar_itens_alimentação()
    imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade',
                     get_itens_alimentação().values())
    cadastrar_chefs()
    imprimir_objetos('Chef : nome, anos de experiência, estrangeiro, data de nascimento',
                     get_chefs().values())
    cadastrar_menus()
    imprimir_objetos('Menu : nome, tipo, armazenamento', get_menus().values())

    for menu in get_menus().values():
        print('\n\n=== Menu : ' + str(menu) + ' ===')
        itens_menu = menu.itens_alimentação.values()
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade', itens_menu)

        itens_ordenados = ordenar_objetos_por_um_atributo(objetos=itens_menu,
            atributo_ordenação=lambda item: item.nível_popularidade, ordenação_decrescente=True)
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade'
                         + ' --- por ordem decrescente de nível de popularidade', itens_ordenados)

        itens_ordenados = ordenar_objetos_por_um_atributo(objetos=itens_menu,
            atributo_ordenação=lambda item: item.preço, ordenação_decrescente=True)
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade'
                         + ' --- por ordem decrescente de preço', itens_ordenados)

        itens_ordenados = ordenar_objetos_por_dois_atributos(objetos=itens_menu,
            atributo1=lambda item: item.nível_popularidade,
            atributo2=lambda item: item.preço, ordenação_decrescente=True)
        imprimir_objetos('Item Alimentação : nome, preço, avaliação, nível de popularidade'
                         + ' --- por ordem decrescente de nível de popularidade e preço', itens_ordenados)

    cadastrar_restaurantes()
    print('\n\n=== Restaurantes ===')
    imprimir_objetos('Restaurante : local, menu, chef', get_restaurantes())