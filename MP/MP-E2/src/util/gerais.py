def imprimir_objetos(cabeçalho, objetos):
    print('\n' + cabeçalho)
    for índice, objeto in enumerate(objetos):
        formato = '{:<5} {}'
        print(formato.format(str(índice + 1) + ' - ', str(objeto)))

def ordenar_objetos_por_um_atributo(objetos, comparador):
    objetos_ordenados = []
    for objeto_desordenado in objetos:
        ordenou_objeto = False
        for índice, objeto_ordenado in enumerate(objetos_ordenados):
            if comparador(objeto_desordenado, objeto_ordenado):
                objetos_ordenados.insert(índice, objeto_desordenado)
                ordenou_objeto = True
                break
        if not ordenou_objeto: objetos_ordenados.append(objeto_desordenado)
    return objetos_ordenados
