from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()


    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho","agosto","setembro","outubro","novembro","desembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        print (mes_cadastro)
        return meses_do_ano[mes_cadastro - 1 ]

    def dia_semana(self):
        dia_da_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        print(dia_semana)
        return dia_da_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def __str__(self):
        return self.format_data()

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=30) - self.momento_cadastro
        return tempo_cadastro