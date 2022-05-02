import pandas as pd
from busca_planilha import buscaPlanilha

class limpaPlanilha:
    def __init__(self):
        self.__caminho = buscaPlanilha().caminho

    @property
    def caminho(self):
        return self.__caminho

    def dataframe(self):
        return pd.read_csv(self.caminho)


if __name__ == '__main__':
    planilha_base = limpaPlanilha()

    sub_grupos = [x for x in planilha_base.dataframe().iloc[:, 0]]
    quantidade = [x for x in planilha_base.dataframe().iloc[:, 2]]
    faturamento = [x for x in planilha_base.dataframe().iloc[:, 3]]
    custo = [x for x in planilha_base.dataframe().iloc[:, 4]]
    despesa_total = [x for x in planilha_base.dataframe().iloc[:, 5]]
    despesa_unitaria = [x for x in planilha_base.dataframe().iloc[:, 6]]
    print(sub_grupos)
    print(quantidade)
    print(faturamento)
    print(despesa_total)
    print(despesa_unitaria)
