"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de
programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o
final da votação, o programa deverá exibir:


-O total de votos computados;
-Os númeos e respectivos votos de todos os jogadores que receberam votos;
-O percentual de votos de cada um destes jogadores;
-O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada
jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das
informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no
disco, obedecendo a mesma disposição apresentada na tela.

"""






with open("resultado.txt", 'w') as f:
    jogador = []
    contagem = 0
    print('##Enquete: Qual foi o melhor jogador?##')
    print('Digite um número de 1 à 23!\n')
    while True:
        pergunta = int(input('Numero do jogador (0=fim): '))
        contagem += 1
        if pergunta == 0:
            contagem -= 1
            break
        jogador.append(pergunta)
        if pergunta > 23:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')


    def percentual(numero_de_votos_por_jogador, total_de_votos):
        numero_de_votos_por_jogador = jogador.count(numero_de_votos_por_jogador)
        total_de_votos = len(total_de_votos)
        porcentagem = (numero_de_votos_por_jogador / total_de_votos * 100)
        return porcentagem


        # pra pegar valores nao duplicados por causa do loop
        # https://www.adamsmith.haus/python/answers/how-to-remove-duplicates-from-a-list-while-keeping-its-order-in-python
    print('\nResultado da votação:')
    f.write('\nResultado da Votação:\n')
    f.write('\n')
    print(f'\nForam computados {contagem} votos')
    f.write(f'Foram computados {contagem} votos\n')

    j, v, p = 'Jogador', 'Votos', '%'
    print(f'\n{j:^6} {v:^9} {p:^5}')
    f.write('\n')
    f.write(f'{j:^6} {v:^9} {p:^5}')

    valores_nao_duplicados = []

    for valor in jogador:
        if valor not in valores_nao_duplicados:
            valores_nao_duplicados.append(valor)
            print(f'{valor:^7} {jogador.count(valor):^9} {percentual(valor, jogador):.1f}%')
            f.write('\n')
            f.write(f'{valor:^7} {jogador.count(valor):^9} {percentual(valor, jogador):.1f}%')

    print(f'\nO melhor jogador foi o número {max(jogador, key=jogador.count)}, com '
          f'{jogador.count(max(jogador, key=jogador.count))} votos, correspondendo a '
          f'{(jogador.count(max(jogador, key=jogador.count))) / len(jogador) * 100:.1f}% do total de votos.')
    f.write('\n')
    f.write(f'\nO melhor jogador foi o número {max(jogador, key=jogador.count)}, com '
          f'{jogador.count(max(jogador, key=jogador.count))} votos, correspondendo a '
          f'{(jogador.count(max(jogador, key=jogador.count))) / len(jogador) * 100:.1f}% do total de votos.')
f.close()