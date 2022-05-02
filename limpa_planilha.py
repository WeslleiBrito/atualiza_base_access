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
    print(sub_grupos)
    print(quantidade)
