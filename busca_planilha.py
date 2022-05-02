from tkinter import filedialog

class buscaPlanilha:
    def __init__(self):
        self.__caminho = self.busca()

    @property
    def caminho(self):
        return self.__caminho

    def busca(self):
        return filedialog.askopenfilename(filetypes=(('Arquivo excel', '*.csv'), ('', '')))


if __name__ == '__main__':
    arquivo = buscaPlanilha()
    print(arquivo.caminho)


