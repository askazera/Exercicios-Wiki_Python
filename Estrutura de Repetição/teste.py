"""
exercicio de tabuada

"""
num = int(input('digite um numero:'))
x = 0

for x in range(1, 11):
    print(num, 'X', x, '=', num * x)
    x += 1
