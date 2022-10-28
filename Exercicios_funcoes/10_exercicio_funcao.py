"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre
2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira
jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu
"Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se
tirar um 7 antes de tirar este Ponto novamente.



"""
import random
import time

natural = [7, 11]
craps = [2, 3, 12]
ponto = [4, 5, 6, 8, 9, 10]


def jogo(natural, craps, ponto):
    jogada = random.randint(2, 12)
    print('Jogando os dados...')
    print(jogada)
    time.sleep(0.8)
    if jogada in natural:
        time.sleep(0.8)
        print('Natural! Ganhou!')
        exit()
    if jogada in craps:
        time.sleep(0.8)
        print('CRAPS! Perdeu!')
        exit()
    if jogada in ponto:
        time.sleep(0.8)
        print('Ponto!')
        jogada2 = 0
        while jogada != jogada2:
            jogada2 = random.randint(2, 12)
            if jogada2 == 7:
                time.sleep(0.8)
                print(f'{jogada2} Perdeu!')
                break
            if jogada != jogada2:
                time.sleep(0.8)
                print(f'Jogando novamente: {jogada2}')
        else:
            time.sleep(0.8)
            print(f'{jogada2} Ganhou! Número igual!')

jogo(natural,craps,ponto)

while True:
    x = input('Deseja jogar novamente? ').upper()
    if x == 'S':
        jogo(natural, craps, ponto)
    else:
        print('Bye bye!')
        break