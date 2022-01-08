class Data:
    def __init__(self, dia, mes, ano):
        self.dia = int(dia)
        self.mes = int(mes)
        self.ano = int(ano)

    def formatada(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))
