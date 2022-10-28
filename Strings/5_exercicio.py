"""

Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
"""

palavra = input('Digite uma palavra:')

print(palavra)
for i in range(len(palavra)):
    i += 1
    print(palavra[:-i])

'''
#Outra forma de resolver abaixo

palavra = input('Digite uma palavra:')

while palavra != '':
    print(palavra)
    palavra = palavra[:-1]
'''
