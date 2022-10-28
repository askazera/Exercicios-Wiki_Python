"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""

letra = str.upper(input('Letra:'))
lista = str(list['A', 'E', 'I', 'O', 'U'])

if letra in lista:
    print('Vogal')
else:
    print('Consoante')
