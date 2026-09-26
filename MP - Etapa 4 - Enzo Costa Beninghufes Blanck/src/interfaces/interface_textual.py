from src.util.gerais import imprimir_objetos, imprimir_títulos, ordenar_objetos_por_um_atributo, ordenar_objetos_por_dois_atributos
from src.entidades.chef import get_chefs
from src.entidades.item_alimentação import get_itens_alimentação
from src.entidades.menu import get_menus
from src.entidades.restaurante import get_restaurantes


def loop_operações_projeto():
    arquivo_saída = open(file='../../dados/arquivo_saída.txt', mode='w', encoding='utf-8')
    sair_loop = False
    while not sair_loop:
        operações_str = ('\nRestaurante com Ítens de Alimentação em um Menu criados por um Chef'
                         + '\n1 - Chefs'
                         + '\n2 - Ítens de Alimentação'
                         + '\n3 - Menus'
                         + '\n4 - Restaurantes'
                         + '\n5 - Ítens de Alimentação dos Menus')
        print(operações_str)
        arquivo_saída.write(operações_str + '\n')
        questão = 'número da operação do Projeto a ser executada'
        operação = ler_int_positivo(questão)
        questão_resposta = questão + ' : ' + str(operação) + '\n'
        arquivo_saída.write(questão_resposta)
        if operação is None: break
        elif operação == 1:
            imprimir_objetos(cabeçalho='Chefs : nome, anos_experiência, estrangeiro, data_nascimento',
                             objetos=get_chefs().values(), arquivo=arquivo_saída)
        elif operação == 2:
            imprimir_objetos(cabeçalho='Ítens de Alimentação : nome, preço, avaliação, nível_popularidade',
                             objetos=get_itens_alimentação().values(), arquivo=arquivo_saída)
        elif operação == 3:
            imprimir_objetos(cabeçalho='Menus : nome, tipo, armazenamento',
                             objetos=get_menus().values(), arquivo=arquivo_saída)
        elif operação == 4:
            imprimir_objetos(cabeçalho='Restaurantes : local, menu, chef',
                             objetos=get_restaurantes(), arquivo=arquivo_saída)
        elif operação == 5:
            loop_títulos_menus(arquivo_saída)
        sair_loop = ler_sair_loop('operações do Projeto')
    arquivo_saída.close()


def loop_títulos_menus(arquivo_saída):
    sair_loop = False
    ids_menus = list(get_menus().keys())
    while not sair_loop:
        imprimir_títulos(cabeçalho='Selecionar o Menu', títulos=ids_menus, arquivo=arquivo_saída)
        questão = 'número do Menu a ser executado'
        índice_menu = ler_int_positivo(questão)
        questão_resposta = questão + ' : ' + str(índice_menu) + '\n'
        arquivo_saída.write(questão_resposta)
        if índice_menu is None: break
        elif índice_menu in range(1, len(ids_menus) + 1):
            menu_selecionado = get_menus()[ids_menus[índice_menu - 1]]
            itens_menu = menu_selecionado.itens_alimentação.values()
            print('\n\n=== Menu : ' + menu_selecionado.título() + ' ===')
            arquivo_saída.write('\n\n=== Menu : ' + menu_selecionado.título() + ' ===\n')
            imprimir_objetos('Ítens de Alimentação : nome, preço, avaliação, nível_popularidade',
                             itens_menu, arquivo_saída)
            imprimir_objetos('Ítens de Alimentação : nome, preço, avaliação, nível_popularidade'
                             + ' -- ordenação decrescente por nível_popularidade',
                             ordenar_objetos_por_um_atributo(objetos=itens_menu,
                                 atributo_ordenação=lambda item: item.nível_popularidade,
                                 ordenação_decrescente=True), arquivo_saída)
            imprimir_objetos('Ítens de Alimentação : nome, preço, avaliação, nível_popularidade'
                             + ' -- ordenação decrescente por preço',
                             ordenar_objetos_por_um_atributo(objetos=itens_menu,
                                 atributo_ordenação=lambda item: item.preço,
                                 ordenação_decrescente=True), arquivo_saída)
            imprimir_objetos('Ítens de Alimentação : nome, preço, avaliação, nível_popularidade'
                             + ' -- ordenação decrescente por nível_popularidade e preço',
                             ordenar_objetos_por_dois_atributos(objetos=itens_menu,
                                 atributo1=lambda item: item.nível_popularidade,
                                 atributo2=lambda item: item.preço,
                                 ordenação_decrescente=True), arquivo_saída)
        sair_loop = ler_sair_loop('títulos dos Menus')


def ler_int_positivo(dado):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0: return None
        if len(string) > 0:
            int_positivo = int(string)
            if int_positivo > 0: return int_positivo
    except ValueError: pass
    print('Erro na leitura/conversão do inteiro positivo: ' + dado)
    return None


def ler_sair_loop(loop):
    try:
        sair = input('\n-- sair do loop de ' + loop + ' [S]: ')
        if sair == 'S': return True
        else: return False
    except IOError: pass
    return False