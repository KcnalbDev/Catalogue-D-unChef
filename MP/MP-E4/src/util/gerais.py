def imprimir_objetos(cabeçalho, objetos, arquivo=None):
    print('\n' + cabeçalho)
    if arquivo is not None: arquivo.write('\n' + cabeçalho + '\n')
    for índice, objeto in enumerate(objetos):
        formato = '{} {}'
        string = formato.format(f'{(índice + 1):2d} - ', str(objeto))
        print(string)
        string += '\n'
        if arquivo is not None: arquivo.write(string)

def imprimir_títulos(cabeçalho, títulos, arquivo=None):
    print('\n' + cabeçalho)
    if arquivo is not None: arquivo.write('\n' + cabeçalho + '\n')
    for índice, título in enumerate(títulos):
        formato = '{} {}'
        string = formato.format(f'{(índice + 1):2d} - ', título)
        print(string)
        string += '\n'
        if arquivo is not None: arquivo.write(string)

def ordenar_objetos_por_um_atributo(objetos, atributo_ordenação, ordenação_decrescente):
    objetos_ordenados = list(objetos)
    objetos_ordenados.sort(key=atributo_ordenação, reverse=ordenação_decrescente)
    return objetos_ordenados

def ordenar_objetos_por_dois_atributos(objetos, atributo1, atributo2, ordenação_decrescente):
    objetos_ordenados_atributo1 = list(objetos)
    objetos_ordenados_atributo1.sort(key=atributo1, reverse=ordenação_decrescente)
    objetos_ordenados_atributo1_atributo2 = []
    último_atributo1 = atributo1(objetos_ordenados_atributo1[0])
    objetos_mesmo_atributo1 = []
    for objeto in objetos_ordenados_atributo1:
        if atributo1(objeto) == último_atributo1: objetos_mesmo_atributo1.append(objeto)
        else:
            objetos_mesmo_atributo1.sort(key=atributo2, reverse=ordenação_decrescente)
            for objeto_mesmo_atributo1 in objetos_mesmo_atributo1:
                objetos_ordenados_atributo1_atributo2.append(objeto_mesmo_atributo1)
            objetos_mesmo_atributo1 = [objeto]
            último_atributo1 = atributo1(objeto)
    objetos_mesmo_atributo1.sort(key=atributo2, reverse=ordenação_decrescente)
    for objeto_mesmo_atributo1 in objetos_mesmo_atributo1:
        objetos_ordenados_atributo1_atributo2.append(objeto_mesmo_atributo1)
    return objetos_ordenados_atributo1_atributo2