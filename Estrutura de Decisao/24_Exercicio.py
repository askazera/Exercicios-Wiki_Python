"""

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado
da operação deve ser acompanhado de uma frase que diga se o número é:

a) par ou ímpar;
b) positivo ou negativo;
c) inteiro ou decimal.


"""

n1 = float(input('numero 1:'))
n2 = float(input('numero 2:'))

op = int(input('Qaul operação deseja realizar?\n1- soma\n2- subtração\n3- multiplicação\n4- divisão\n'))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
a = 'impar'
b = 'positivo'
c = 'inteiro'


if op == 1:
    op = soma
elif op == 2:
    op = sub
elif op == 3:
    op = mult
elif op == 4:
    op = div

print('Resultado:', op)


if op % 2 == int or op % 2 == 0:
    print('par')
else:
    print(a)
if op < 0:
    print('negativo')
else:
    print(b)
if op != round(op):
    print('decimal')
else:
    print(c)
