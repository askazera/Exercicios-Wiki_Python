"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe
também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.


"""
import time

n1 = input('String 1: ')
n2 = input('String 2: ')

time.sleep(0.5)
print(n1)
print(n2)
time.sleep(0.8)
print(f'Tamanho da string 1: {len(n1)}')
print(f'Tamanho da string 2: {len(n2)}')

time.sleep(0.8)
if n1 == n2:
    print('As strings possuem o mesmo conteúdo')
else:
    print('As string não possuem o mesmo conteúdo')

time.sleep(0.8)
if len(n1) == len(n2):
    print('As strings possuem o mesmo tamanho')
else:
    print('As strings não possuem o mesmo tamanho')
