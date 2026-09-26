def imprimir_objetos(cabeçalho, objetos):
    print('\n' + cabeçalho)
    for índice, objeto in enumerate(objetos):
        formato = '{:<5} {}'
        print(formato.format(str(índice + 1) + ' - ', str(objeto)))
