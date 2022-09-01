from datetime import datetime, timedelta
from datasBr import DatasBr

"""cadastro = DatasBr()

print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)"""

"""
hoje = datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje_formatado)"""

hoje = DatasBr()
print(hoje.tempo_cadastro())