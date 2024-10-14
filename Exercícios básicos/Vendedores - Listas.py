"""
Uma loja deseja avaliar o desempenho de seus vendedores. Crie um programa que:

- Solicite ao usuário o número total de vendedores da loja.
- Para cada vendedor, peça ao usuário o nome do vendedor e o total de vendas realizadas no ano.
- Determine o vendedor com o maior volume de vendas e o vendedor com o menor volume.
- Exiba o nome de todos os vendedores e suas vendas totais, destacando o vendedor com as vendas mais altas e o vendedor com as vendas mais baixas.
"""

num_vendedores = int(input('Informe o total de vendedores: '))

list_vendedor=[]
list_vendas=[]
for i in range (0,num_vendedores):
    vendedor = input('Informe o nome do vendedor: ')
    vendas = float(input('Informe o total de vendas:'))
    list_vendedor.append(vendedor)
    list_vendas.append(vendas)


for i in range (0, num_vendedores):
    if list_vendas[i] == max(list_vendas):
        print (f'{list_vendedor[i]}: {list_vendas[i]} - Maior volume de vendas')
    elif list_vendas[i] == min(list_vendas):
        print (f'{list_vendedor[i]}: {list_vendas[i]} - Menor volume de vendas')
    else:
        print (f'{list_vendedor[i]}: {list_vendas[i]}')


