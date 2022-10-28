'''

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''


p1 = str.upper(input('1- Telefonou para a vítima?'))
p2 = str.upper(input('2- Esteve no local do crime?'))
p3 = str.upper(input('3- Mora perto da vítima?'))
p4 = str.upper(input('4- Devia para a vítima?'))
p5 = str.upper(input('5- Já trabalhou com a vítima?'))


var = 0

if p1 == 'SIM':
    var = var+1
if p2 == 'SIM':
    var = var+1
if p3 == 'SIM':
    var = var+1
if p4 == 'SIM':
    var = var+1
if p5 == 'SIM':
    var = var+1

if var == 2:
    print('Suspeito')
if var == 3 or var == 4:
    print('Cumplice')
if var == 5:
    print('Assassino')
if var < 2:
    print('Inocente')
