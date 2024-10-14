"""Uma academia deseja fazer um censo entre seus clientes para descobrir o mais alto, o
mais baixo, o mais pesado e o mais leve. Antes de iniciar é necessário perguntar ao
usuário quantos clientes há na academia. Após isto, o sistema irá receber, de cada um
dos clientes da academia:
● seu código;
● sua altura;
● e seu peso.

Ao encerrar o programa devem ser informados:
● o código, altura e peso do cliente mais alto
● o código, altura e peso do cliente mais baixo
● o código, altura e peso do cliente mais pesado
● o código, altura e peso do cliente mais leve
● a média das alturas de todos os clientes
● a média dos pesos de todos os clientes

O foco desse programa será a utilização de Estruturas de repetições e Estruturas Condicionais
"""

clientes = int(input('Informe a quantidade de clientes: '))
i = 0
alt_total = 0
peso_total=0
while i < clientes:

    if i == 0:
        cod = input(f'Informe o código do {i+1}º cliente: ')
        altura = float(input('Informe a altura do cliente: '))
        peso = float (input('Informe o peso do cliente: '))
        alt_max_a = altura
        alt_max_p = peso
        alt_max_c = cod
        alt_min_a = altura
        alt_min_p = peso
        alt_min_c = cod
        peso_max_p = peso
        peso_max_a = altura
        peso_max_c = cod
        peso_min_p = peso
        peso_min_a = altura
        peso_min_c = cod
        alt_total += altura
        peso_total += peso
        i +=1
    else:
        cod = input(f'Informe o código do {i+1}º cliente: ')
        altura = float(input('Informe a altura do cliente: '))
        peso = float(input('Informe o peso do cliente: '))
        if peso > peso_max_p:
            peso_max_p = peso
            peso_max_a = altura
            peso_max_c = cod
        elif peso < peso_min_p:
            peso_min_p = peso
            peso_min_a = altura
            peso_min_c = cod
        if altura > alt_max_a:
            alt_max_a = altura
            alt_max_p = peso
            alt_max_c = cod
        elif altura < alt_min_a:
            alt_min_a = altura
            alt_min_p = peso
            alt_min_c = cod
        alt_total += altura
        peso_total += peso
        i += 1


print (f' O cliente mais alto tem código {alt_max_c}, altura de {alt_max_a}m e peso de {alt_max_p}kg')
print (f' O cliente mais baixo tem código {alt_min_c}, altura de {alt_min_a}m e peso de {alt_min_p}kg')
print (f' O cliente mais leve tem código {peso_min_c}, altura de {peso_min_a}m e peso de {peso_min_p}kg')
print (f' O cliente mais pesado tem código {peso_max_c}, altura de {peso_max_a}m e peso de {peso_max_p}kg')
print (f' A média das alturas é {round(alt_total/clientes,2)}m')
print (f' A média dos pesos é {peso_total/clientes}kg')