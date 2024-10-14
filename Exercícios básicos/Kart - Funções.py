"""Uma pista de Kart permite 3 voltas para cada um dos 4 corredores. No programa principal, implemente um código que leia o nome do corredor e todos
os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Implemente duas funções:

1. Uma função chamada calcular_media que recebe uma lista de tempos como parâmetro e retorna a média desses tempos.
2. Uma função chamada encontrar_campeao que recebe o dicionário de tempos como parâmetro e usa a função calcular_media para calcular a média de tempo de cada corredor.
A função deve identificar o campeão (corredor com a menor média de tempo) e retornar o nome do campeão e sua média de tempo com duas casas decimais.
No final do programa principal, exiba o nome do campeão em maiúsculas e sua média de tempo com duas casas decimais."""

def calcular_media(lista:list):
    media = sum(lista)/len(lista)
    return media

def encontrar_campeao(tempos:dict):
    campeao =''
    melhor_tempo = 10000000000
    for k,v in tempos.items():
        media = calcular_media(v)
        if media < melhor_tempo:
            melhor_tempo = media
            campeao = k
    print(f'O Campeão é {campeao.upper()} com média de tempo de {melhor_tempo:.2f} segundos')

dic={}
for i in range (0,4):
    nome = input('Informe o nome do corredor: ')
    tempo1 = float(input('Informe o tempo da primeira volta: '))
    tempo2 = float(input('Informe o tempo da segunda volta: '))
    tempo3 = float(input('Informe o tempo da terceira volta: '))
    dic[nome]=[tempo1,tempo2,tempo3]

encontrar_campeao(dic)


