from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta


def proximo_dia_util():
    dia = datetime.today()
    while dia.weekday() in [6, 7]:
        dia += timedelta(days=1)
    return dia + timedelta(days=14)


def primeira_data_de_vencimento(_data_de_vencimento, carencia):
    _data_de_vencimento = somar_meses(_data_de_vencimento, carencia)

    if _data_de_vencimento.day > 28:
        _data_de_vencimento = _data_de_vencimento.replace(day=28)

    return _data_de_vencimento


def somar_meses(data, n_meses):
    return data + relativedelta(months=n_meses)


data_de_emissao = proximo_dia_util()
print("data_de_emissao      ", data_de_emissao)

data_de_vencimento__1 = primeira_data_de_vencimento(data_de_emissao, 6)
print("data_de_vencimento__1", data_de_vencimento__1)

ultima_data_de_vencimento = somar_meses(data_de_vencimento__1, 144)

if ultima_data_de_vencimento.day > 28:
    ultima_data_de_vencimento = ultima_data_de_vencimento.replace(day=28)

print(f"data_de_vencimento__{144}", ultima_data_de_vencimento)

print("...")

ultima_data_de_vencimento = somar_meses(data_de_vencimento__1, 36 - 1)
print("data_de_vencimento_36", ultima_data_de_vencimento)
