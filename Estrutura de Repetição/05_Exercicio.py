'''

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
'''

print('Insira no país A a menor pupulação')
a = float(input('População do país A:'))
tx_a = float(input('Taxa de crescimento de A:'))
b = float(input('População do país B:'))
tx_b = float(input('Taxa de crescimento de B:'))
ano = 0

while a <= b:
    a += a * (tx_a * 0.01)
    b += b * (tx_b * 0.01)
    ano += 1
print('A ultrapassa ou se iguala a B em:', ano, 'anos')

resp = str.upper(input('Deseja repetir a operação?\nS- SIM\nN- NÃO\n:'))


while resp == 'S':
    print('Insira no país A a menor pupulação')
    a = float(input('População do país A:'))
    tx_a = float(input('Taxa de crescimento de A:'))
    b = float(input('População do país B:'))
    tx_b = float(input('Taxa de crescimento de B:'))
    ano = 0

    while a <= b:
        a += a * (tx_a * 0.01)
        b += b * (tx_b * 0.01)
        ano += 1
    print('A ultrapassa ou se iguala a B em:', ano, 'anos')

    resp = str.upper(input('Deseja repetir a operação?\nS- SIM\nN- NÃO\n:'))

else:
    print('Operação encerrada')