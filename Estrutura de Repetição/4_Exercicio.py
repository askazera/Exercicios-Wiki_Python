'''

Supondo que a popula��o de um pa�s A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
popula��o de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Fa�a um programa que calcule e escreva o
n�mero de anos necess�rios para que a popula��o do pa�s A ultrapasse ou iguale a popula��o do pa�s B, mantidas as taxas
de crescimento.
'''

a = 80.000
b = 200.000
ano = 0

while a <= b:
    a += a * 0.03
    b += b * 0.015
    ano += 1
print('A ultrapassa ou iguala a B em:', ano)
