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

    @property
    def sub_grupos(self):
        return self.__sub_grupos()

    @property
    def sub_grupo_unitario(self):
        return self.__sub_grupo_unitario()

    @property
    def grupos(self):
        return self.__grupos()

    @property
    def quantidades(self):
        return self.__quantidades()

    @property
    def faturamentos(self):
        return self.__faturamentos()

    @property
    def custo(self):
        return self.__custos()

    def __dataframe(self):
        return pd.read_excel(self.caminho, 'A')

    def __coluna(self, nome_coluna):
        return [x for x in self.planilha[f'{nome_coluna}']][:-2]

    def __coluna_unitaria(self, nome_coluna):
        return [x for x in self.planilha[f'{nome_coluna}'].unique()][:-2]

    def __sub_grupos(self):
        return self.__coluna('Subgrupo')

    def __sub_grupo_unitario(self):
        return self.__coluna_unitaria('Subgrupo')

    def __grupos(self):
        return self.__coluna('Grupo')

    def __quantidades(self):
        return self.__coluna('Qtd. Vendida')

    def __faturamentos(self):
        return self.__coluna('Valor Total')

    def __custos(self):
        custo = []
        custos = self.__coluna('Vr. Custo')
        for index, quantidade in enumerate(self.quantidades):
            x = quantidade * custos[index]
            custo.append(x)
        return custo


if __name__ == '__main__':

    planExcel = limpaPlanilhaExcel()
    sub_grupos_total = planExcel.sub_grupos
    sub_grupos = planExcel.sub_grupo_unitario
    grupos = planExcel.grupos
    quantidades = planExcel.quantidades
    faturamentos = planExcel.faturamentos
    custos = planExcel.custo
    print('Grupos:', grupos)
    print('Quantidades:', quantidades)
    print('Faturamentos:', faturamentos)
    print(f'Custos: {custos}')
    valor = 0.0
    cst = 0.0

    valores_subgrupos = dict()
    custo_subgrupos = dict()

    inicio = time.time()
    for subgrupo in sub_grupos:
        for index, vr in enumerate(sub_grupos_total):
            if vr == subgrupo:
                valor += faturamentos[index]
                cst += custos[index]

        valores_subgrupos[f'{subgrupo}'] = valor
        custo_subgrupos[f'{subgrupo}'] = cst
        valor = 0.0
        cst = 0.0

    for x in valores_subgrupos.items(), custo_subgrupos.items():
        print(x)

    fim = time.time()
    print(fim - inicio)
