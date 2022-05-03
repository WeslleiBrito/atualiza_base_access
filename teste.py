from valores import valoresExcel, planilhaFinal
import pandas as pd

class UnificandoDados():
    def __init__(self):
        self.__objeto = valoresExcel()

    @property
    def calculo(self):
        return self.__calculo()

    @property
    def planilha(self):
        return self.__planilha()

    @property
    def objeto(self):
        return self.__objeto

    def __calculo(self):

        quantidade = 0.0
        custo = 0.0
        faturamento = 0.0

        quantidades = self.objeto.quantidades
        custos = self.objeto.custo
        faturamentos = self.objeto.faturamentos
        sub_grupos = self.objeto.sub_grupos
        sub_grupo = self.objeto.sub_grupo_unitario

        sub_quantidades = dict()
        sub_custo = dict()
        sub_faturamento = dict()

        for sub in sub_grupo:
            for index, subGrupo in enumerate(sub_grupos):
                if subGrupo == sub:
                    quantidade += quantidades[index]
                    custo += custos[index]
                    faturamento += faturamentos[index]

            sub_quantidades[f'{sub}'] = quantidade
            sub_custo[f'{sub}'] = custo
            sub_faturamento[f'{sub}'] = faturamento

            quantidade = 0.0
            custo = 0.0
            faturamento = 0.0

        return sub_quantidades, sub_custo, sub_faturamento

    def __planilha(self):
        subgrupo = self.objeto.sub_grupo_unitario
        planilha = pd.DataFrame(columns=['SubGrupo', 'Quantidade', 'Custo', 'Faturamento'])
        dados = []
        for sub_grupo in subgrupo:
            dados = [sub_grupo, self.calculo[0][f'{sub_grupo}'], self.calculo[1][f'{sub_grupo}'], self.calculo[2][f'{sub_grupo}']]

            planilha.loc[len(planilha)] = dados

        return planilha


if __name__ == '__main__':

    print(planilhaFinal())
