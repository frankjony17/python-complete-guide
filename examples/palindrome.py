"""
  Escreva um algoritmo que receba um texto como entrada e precisará retornar
  se ele é ou não um palíndromo.
  Sendo 1 para o caso de ser palíndromo e 0 quando não for.

  Explicação:
    O texto pode ser lido tanto da direita para a esquerda como da esquerda para a direita
"""


def is_palindrome(text: str):
    txet = text[::-1]
    output = 0

    if txet == text:
        output = 1

    return output


input_text = str(input("Get text:"))

print(is_palindrome(input_text))
