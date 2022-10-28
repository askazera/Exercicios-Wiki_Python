'''

Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

nome = str(input('Nome:'))

while len(nome) < 4:
    print('Nome inválido! insira um nome maior do que 3 caracteres')
    nome = str(input('Nome:'))


idade = int(input('Idade:'))

while idade > 150:
    print('Idade inválida! insira uma idade até 150 anos')
    idade = int(input('Idade:'))


salario = float(input('Salário:'))

while salario <= 0 or salario != float:
    print('Salário inválido! insira um valor maior que 0')
    salario = float(input('Salário:'))


sexo = str.lower(input('Sexo\nf - Feminino\nm - Masculino\n:'))

while sexo != 'f' and sexo != 'm':
    print('Sexo inválido! insira f ou m')
    sexo = str.lower(input('Sexo\nf - Feminino\nm - Masculino\n:'))

estado_civil = str.lower(input('Estado civil\ns- Solteiro(a)\nc- Casado(a)\nv- Viúvo(a)\nd- Divorciado(a):'))
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    print('Estado civil inválido! Digite a opção correta')
    estado_civil = str.lower(input('Estado civil\ns- Solteiro(a)\nc- Casado(a)\nv- Viúvo(a)\nd - divorciado(a):'))
