from datetime import date

from datetime import date

class Data:
    def __init__(self, dia, mês, ano):
        self.dia = dia
        self.mês = mês
        self.ano = ano

    def __str__(self):
        if self.dia < 10:
            data_str = '0' + str(self.dia)
        else:
            data_str = str(self.dia)
        if self.mês < 10:
            data_str += '/0' + str(self.mês) + '/' + str(self.ano)
        else:
            data_str += '/' + str(self.mês) + '/' + str(self.ano)
        return data_str

    def calcular_idade(self, data_referência=None):
        if data_referência is None:
            dia_atual_str, mês_atual_str, ano_atual_str = date.today().strftime("%d/%m/%Y").split('/')
            dia_referência, mês_referência, ano_referência = int(dia_atual_str), int(mês_atual_str), int(ano_atual_str)
        else:
            dia_referência, mês_referência, ano_referência = data_referência.dia, data_referência.mês, data_referência.ano
        idade = ano_referência - self.ano
        if mês_referência < self.mês or (mês_referência == self.mês and dia_referência < self.dia):
            idade -= 1
        return idade
