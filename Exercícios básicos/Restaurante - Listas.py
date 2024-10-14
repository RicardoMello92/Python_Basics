"""Desenvolva um programa que permita aos usuários avaliarem restaurantes com notas de 0 a 5. Cada restaurante só deve ser inserido uma vez na lista.
Se um restaurante for avaliado mais de uma vez, o programa deve atualizar a nota média do restaurante considerando todas as avaliações fornecidas até o momento,
mas o restaurante não deve ser adicionado novamente à lista.

O programa deve:
● Solicitar o nome do restaurante ou digitar “PARE” para finalizar.
● Solicitar a nota dada pelo usuário (de 0 a 5).
● Se o restaurante já foi avaliado anteriormente, atualizar a nota média

Ao final, o programa deve mostrar o restaurante com a maior nota média e o restaurante com a menor nota média.

O foco desse programa é a utilização de listas e manipulação de Strings"""


nome=''
list_nome=[] #lista com nomes
list_nota=[] #lista com as médias das notas
list_count=[] #lista com as contagens de restaurantes avaliados

while nome != 'pare':
    nome = input('Informe o nome do restaurante. Escreva pare para sair. ').lower()
    if nome.lower() =='pare':
        break
    else:
        nota = float(input('Informe a nota do restaurante (0 a 5):'))
        while nota <0 or nota >6:
          print ('Nota inválida. Informe uma nova nota: ')
          nota = float(input('Informe a nota do restaurante (0 a 5):'))
    if nome in list_nome:
        i = list_nome.index(nome) #localizar o indice do restaurante avaliado
        list_count[i] += 1 #somar 1 na contagem
        list_nota[i] = (list_nota[i]+nota)/list_count[i] # atualizar a média do restaurante

    else:
        list_nome.append(nome)
        list_count.append(1)
        list_nota.append(nota)

max_i = list_nota.index(max(list_nota))
min_i = list_nota.index(min(list_nota))

print(f'Restaurante com a maior nota: {list_nome[max_i].title()} com nota {max(list_nota)}')
print(f'Restaurante com a menor nota: {list_nome[min_i].title()} com nota {min(list_nota)}')