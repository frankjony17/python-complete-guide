"""
  Write an algorithm that simulates the operation of an electronic ATM.

  Explicação:
    Deverá receber o valor desejado de saque e ele retornará à
    quantidade de cédulas de cada valor.

  As cédulas consideradas pelo caixa eletrônico são: 100, 50, 20, 10, 5 e 2.
  Deve ser retornado a menor quantidade de cédulas possível para o valor do saque.
"""

note_list = [100, 50, 20, 10, 5, 2]


def get_total_note(note: int, valor: int):
    required_note = 0
    resto = valor

    if valor >= note:  # 101
        required_note = valor / note  # 2
        resto = valor % note  # 1

    if resto == 1 or resto == 3:
        required_note -= 1  # 1-5
        resto += note

    return required_note, resto


value = int(input("Get value of money: "))

for note in note_list:
    required_note, resto = get_total_note(note, value)
    value = resto

    if int(required_note) > 0:
        print(f'{int(required_note)} notas de {note}')
