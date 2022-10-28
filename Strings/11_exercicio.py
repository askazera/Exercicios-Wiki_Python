"""
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
"""

import random

print("Bem vindo ao JOGO DA FORCA. Boa sorte!\n")

file = open('palavras.txt', 'r')
arquivo = file.read()
lista_palavras = list(map(str, arquivo.split()))  # transformando cada item em string dentro de uma lista
palavra_escolhida = random.choices(lista_palavras)
palavra = ''.join(palavra_escolhida)  # transformando o item da lista em uma string com join
lista_palavras_escolhidas = []

chances = 6
print(palavra)

while True:
    print(f"Você tem {chances} chances\n")

    for letra in palavra:
        if letra in lista_palavras_escolhidas:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    palpite = input("\nDigite seu palpite ou 'SAIR' para sair do programa: ").lower()

    if palpite == "sair":
        print('Bye bye!')
        break
    elif palpite.isalpha() is False or palpite == '':
        print("\nIsso não é uma letra!")
        continue
    elif palpite in lista_palavras_escolhidas:
        print("\nVocê já tentou essa letra. Tente outra!")
        continue

    lista_palavras_escolhidas.append(
        palpite)  # append esta nessa linha para que o terceiro elif  nao conte ele como ja existente antes do tempo

    if palpite in palavra:
        print("\nAcertou!")
    else:
        print("\nErrou!")
        chances -= 1

    if chances == 0:
        print('Perdeu! Você foi enforcado!')
        break
    elif set(palavra).issubset(set(lista_palavras_escolhidas)):
        print(f"\nYay! Você ganhou!\nA palavra é: {palavra}")
        break

    print('\nPalavras já escolhidas:', lista_palavras_escolhidas)
