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

    def __eq__(self, data):
        if self.dia == data.dia and self.mês == data.mês and self.ano == data.ano: return True
        return False

    def __ne__(self, data): return not self == data

    def __gt__(self, data):
        if self.ano > data.ano: return True
        elif self.ano < data.ano: return False
        if self.mês > data.mês: return True
        elif self.mês < data.mês: return False
        if self.dia > data.dia: return True
        elif self.dia < data.dia: return False
        return False

    def __lt__(self, data):
        if self.ano < data.ano: return True
        elif self.ano > data.ano: return False
        if self.mês < data.mês: return True
        elif self.mês > data.mês: return False
        if self.dia < data.dia: return True
        elif self.ano > data.ano: return False
        return False

    def __ge__(self, data):
        if self < data: return False
        else: return True

    def __le__(self, data):
        if self > data: return False
        else: return True

def converte_str_para_data(data_str):
    dia, mês, ano = data_str.split('/')
    return Data(int(dia), int(mês), int(ano))