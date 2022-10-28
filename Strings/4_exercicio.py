"""

Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

palavra = input('Digite uma palavra: ')

for i in range(len(palavra)):
    i += 1
    print(palavra[:i])
