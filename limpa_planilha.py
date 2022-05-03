import pandas as pd
import time
from busca_planilha import buscaPlanilhaExcel, buscaPlanilhaCsv

class limpaPlanilhaCsv:
    def __init__(self):
        self.__caminho = buscaPlanilhaCsv.caminho

    @property
    def caminho(self):
        return self.__caminho

    def dataframe(self):
        return pd.read_csv(self.caminho, encoding="latin1")


class limpaPlanilhaExcel:
    def __init__(self):
        self.__caminho = buscaPlanilhaExcel().caminho

    @property
    def caminho(self):
        return self.__caminho

    @property
    def planilha(self):
        return self.__dataframe()

    def __dataframe(self):
        return pd.read_excel(self.caminho, 'A')


if __name__ == '__main__':

    planExcel = limpaPlanilhaExcel()
    sub_grupos_total = [subGrupo for subGrupo in planExcel.planilha['Subgrupo']]
    sub_grupos_total = sub_grupos_total[:-2]
    sub_grupos = [sub_grupo for sub_grupo in planExcel.planilha['Subgrupo'].unique()]
    sub_grupos = sub_grupos[:-2]
    faturamentos = [valor for valor in planExcel.planilha['Valor Total']]
    valor = 0.0

    valores_subgrupos = dict()

    inicio = time.time()
    for subgrupo in sub_grupos:
        for index, vr in enumerate(sub_grupos_total):
            if vr == subgrupo:
                valor += faturamentos[index]

        valores_subgrupos[f'{subgrupo}'] = valor
        valor = 0.0

    for x in valores_subgrupos.items():
        print(x)

    fim = time.time()
    print(fim - inicio)
