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

    @property
    def calculos(self):
        return self.__calculos()

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

    def __calculos(self):

        quantidade = 0.0
        custo = 0.0
        faturamento = 0.0

        faturamento_subgrupos = dict()
        custo_subgrupos = dict()
        quantidade_subgrupos = dict()
        indeces = []
        for sub in self.sub_grupo_unitario:
            for indice, subg in enumerate(self.sub_grupos):
                if sub == subg:
                    indeces.append(indice)

            for vr in indeces:
                quantidade += self.quantidades[vr]
                custo += self.custo[vr]
                faturamento += self.faturamentos[vr]
            print(f'SubGrupo: {sub}, Quantidade: {quantidade}, Custo: {custo}, Faturamento: {faturamento}')
            quantidade = 0.0
            custo = 0.0
            faturamento = 0.0
            indeces.clear()

        #     for indice, subGrupo in enumerate(self.sub_grupos):
        #         if sub == subGrupo:
        #             quantidade += self.quantidades[indice]
        #             custo += self.custo[indice]
        #             faturamento += self.faturamentos[indice]
        #
        #     quantidade_subgrupos[f'{sub}'] = quantidade
        #     custo_subgrupos[f'{sub}'] = custo
        #     faturamento_subgrupos[f'{sub}'] = faturamento
        #     print(f'SubGrupo: {sub}, Quantidade: {quantidade}, Custo: {custo}, Faturamento: {faturamento}')
        #     quantidade = 0.0
        #     custo = 0.0
        #     faturamento = 0.0
        #
        # return [quantidade_subgrupos, custo_subgrupos, faturamento_subgrupos]



if __name__ == '__main__':

    planExcel = limpaPlanilhaExcel().calculos

    # sub_grupos_total = planExcel.sub_grupos
    # sub_grupos = planExcel.sub_grupo_unitario
    # grupos = planExcel.grupos
    # quantidades = planExcel.quantidades
    # faturamentos = planExcel.faturamentos
    # custos = planExcel.custo
    #
    # valor = 0.0
    # cst = 0.0
    # qtd = 0.0
    #
    #
    # planilha_pronta = pd.DataFrame(columns=['SubGrupo', 'Quantidade', 'Custo', 'Faturamento'])
    # lista_geral = []
    #
    # inicio = time.time()
    # for subgrupo in sub_grupos:
    #     for index, vr in enumerate(sub_grupos_total):
    #         if vr == subgrupo:
    #             valor += faturamentos[index]
    #             cst += custos[index]
    #             qtd += quantidades[index]
    #
    #     valores_subgrupos[f'{subgrupo}'] = valor
    #     custo_subgrupos[f'{subgrupo}'] = cst
    #     quantidade_subgrupos[f'{subgrupo}'] = qtd
    #     valor = 0.0
    #     cst = 0.0
    #     qtd = 0.0
    # dados = dict()
    # for x in range(0, len(sub_grupos)):
    #     dados = [sub_grupos[x], quantidade_subgrupos[f'{sub_grupos[x]}'], custo_subgrupos[f'{sub_grupos[x]}'], valores_subgrupos[f'{sub_grupos[x]}']]
    #     planilha_pronta.loc[len(planilha_pronta)] = dados
    #
    # fim = time.time()
    # print(print(planilha_pronta))
    # print(sub_grupos)
    # print(fim - inicio)
