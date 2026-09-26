from src.entidades.chef import get_chefs, inserir_chef, Chef
from src.entidades.item_alimentação import get_itens_alimentação, inserir_item_alimentação, ItemAlimentação
from src.util.gerais import imprimir_objetos
from src.util.data import Data

def cadastrar_itens_alimentação():
    inserir_item_alimentação(ItemAlimentação('Lasanha à Bolonhesa', 45.00, 'ótimo', 10))
    inserir_item_alimentação(ItemAlimentação('Fettuccine', 38.00, 'médio', 7))
    inserir_item_alimentação(ItemAlimentação('Canelone de Queijo', 35.00, 'ruim', 6))
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

if __name__ == '__main__':
    print('\nRestaurante com Ítens de Alimentação em um Menu criados por um Chef')
    cadastrar_itens_alimentação()
    imprimir_objetos(cabeçalho = 'Item Alimentação : nome, preço, avaliação, nível de popularidade', objetos = get_itens_alimentação())

    cadastrar_chefs()
    imprimir_objetos(cabeçalho = 'Chef : nome, anos de experiência, estrangeiro, data de nascimento', objetos = get_chefs())