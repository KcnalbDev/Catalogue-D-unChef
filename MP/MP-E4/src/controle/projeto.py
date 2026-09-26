import json
from src.util.data import converte_str_para_data
from src.entidades.chef import Chef, inserir_chef, get_chefs
from src.entidades.item_alimentação import ItemAlimentação, inserir_item_alimentação, get_itens_alimentação
from src.entidades.menu import Menu, inserir_menu, get_menus
from src.entidades.restaurante import criar_restaurante
from src.interfaces.interface_textual import loop_operações_projeto


def carregar_objetos_arquivo():
    arquivo_entrada = open(file='../../dados/arquivo_entrada.json', mode='r', encoding='utf-8')
    arquivo_dict = json.load(arquivo_entrada)

    chefs_dict_list = arquivo_dict['chefs']
    for chef_dict in chefs_dict_list:
        chef = Chef(nome=chef_dict['nome'], anos_experiência=chef_dict['anos_experiência'],
                    estrangeiro=chef_dict['estrangeiro'],
                    data_nascimento=converte_str_para_data(chef_dict['data_nascimento']))
        inserir_chef(chef)

    itens_dict_list = arquivo_dict['itens_alimentação']
    for item_dict in itens_dict_list:
        item = ItemAlimentação(nome=item_dict['nome'], preço=item_dict['preço'],
                               avaliação=item_dict['avaliação'],
                               nível_popularidade=item_dict['nível_popularidade'])
        inserir_item_alimentação(item)

    menus_dict = arquivo_dict['menus']
    for menu_dict in menus_dict.values():
        menu = Menu(nome=menu_dict['nome'], tipo=menu_dict['tipo'],
                    armazenamento=menu_dict['armazenamento'])
        inserir_menu(menu)
        nomes_itens_list = menu_dict['nomes_itens_alimentação']
        menu.inserir_itens_alimentação(nomes_itens_list)

    restaurantes_dict_list = arquivo_dict['restaurantes']
    for restaurante_dict in restaurantes_dict_list:
        criar_restaurante(local=restaurante_dict['local'],
                          nome_menu=restaurante_dict['nome_menu'],
                          nome_chef=restaurante_dict['nome_chef'])

    arquivo_entrada.close()


if __name__ == '__main__':
    carregar_objetos_arquivo()
    loop_operações_projeto()