"""


Resolução da Questão Desafio: Criação de um sistema CRUD (Create, Read, Update, Delete) em Python para cadastros de items.
A solução utilizada foi a criação de um dicionário para armazenar os registros onde a chave é o código do produto e os valores são as características (Nome, Descrição, Preço e Quantidade) armazenadas como um outro dicionário.
As opções oferecidas aos usuários foram: Cadastrar item, Atualizar Item, Consultar Item, Listar todos os itens, Remover Item, Informar valor total do estoque, Informar valor em estoque de um determinado produto.
Foram usadas funções para realizar as ações de acordo com a escolha do usuário.
"""
dic={}

entrada =''

#Função para cadastrar os itens no sistema
def cadastrar_item():
  cod = input('Informe o código do produto: ')
  if cod in dic:
    print ("""Código já existente

    """)
  else:
    nome = input('Informe o nome do produto: ')
    descricao = input('Informe a descrição do produto: ')
    preco = float(input('Informe o preço do produto: '))
    quantidade = int(input('Informe a quantidade do produto: '))
    print ("""Produto adicionado com sucesso

    """)
    dic[cod]={'nome':nome, 'descrição':descricao,'preço':preco,'quantidade': quantidade }



#Função para atualizar os itens no sistema filtrando por código ou nome
def atualizar_item():
  escolha = input("""Escolha o método de escolha:

  1- Código
  2- Nome

  """)

  if escolha == '1':
    cod = input('Informe o código do produto a ser atualizado ')
    if cod in dic:
      alteracao = input("""
      Informe o que será alterado:
      1 - Código
      2 - Nome
      3 - Descrição
      4 - Preço
      5 - Quantidade

      """)

      if alteracao == '2':
        novo_nome = input("""Informe o novo nome do produto:

        """)
        dic[cod]['nome']=novo_nome
      elif alteracao == '3':
        nova_descricao = input('Informe a nova descrição do produto: ')
        dic[cod]['descrição']=nova_descricao
      elif alteracao == '4':
        novo_preco = int(input('Informe o novo preço do produto: '))
        dic[cod]['preço']=novo_preco
      elif alteracao == '5':
        nova_quantidade = int(input('Informe a nova quantidade do produto: '))
        dic[cod]['quantidade']=nova_quantidade
      elif alteracao == '1':
        novo_cod = input('Informe o novo código do produto: ')
        dic[novo_cod] = dic.pop(cod)
      print("""Produto atualizado

    """)
    else:
      print ("""Produto não encontrado. Informe novamente

      """)
      cod = input("""Informe o código do produto a ser atualizado:

      """)


  elif escolha == '2':
    nome = input("""Informe o nome do produto a ser atualizado

    """)
    for k,v in dic.items():
      if v['nome']==nome:
        cod = k
      alteracao = input("""
      Informe o que será alterado:
      1 - Código
      2 - Nome
      3 - Descrição
      4 - Preço
      5 - Quantidade

      """)

    if alteracao == '2':
      novo_nome = input('Informe o novo nome do produto: ')
      dic[cod]['nome']=novo_nome
    elif alteracao == '3':
      nova_descricao = input('Informe a nova descrição do produto: ')
      dic[cod]['descrição']=nova_descricao
    elif alteracao == '4':
      novo_preco = int(input('Informe o novo preço do produto: '))
      dic[cod]['preço']=novo_preco
    elif alteracao == '5':
      nova_quantidade = int(input('Informe a nova quantidade do produto: '))
      dic[cod]['quantidade']=nova_quantidade
    elif alteracao == '1':
      novo_cod = input('Informe o novo código do produto: ')
      dic[novo_cod] = dic.pop(cod)
    print ("""Produto alterado

    """)


#Função para consultar os items filtrando por código ou nome
def consultar_item():

  escolha = input("""Escolha o método de escolha:

  1- Código
  2- Nome

  """)
  if escolha == '1':
    cod = input('Informe o código do produto a ser atualizado: ')
    if cod in dic:
      print (f"""{dic[cod]}

             """)
    else:
      print ("""Produto não encontrado

      """)
  elif escolha == '2':
    nome = input('Informe o nome do produto a ser atualizado: ')
    for k,v in dic.items():
      if v['nome']==nome:
        print (f"""{dic[k]}

               """)
  else:
    print(""" Escolha incorreta

    """)

#Função para listar todos os produtos disponíveis
def listar_todos():
  for k,v in dic.items():
    print (k,v)
    print()



#Função para remover o produto do cadastro com base no código
def remover_item():

  cod = input('Informe o código do produto a ser deletado: ')
  if cod in dic:
    del dic[cod]
    print ("""Código deletado

    """)
  else:
    print (""" Produto não encontrado

   """)


#Função para cálculo do valor estoque total de produtos
def valor_total_estoque():
      total = 0
      for i in dic.keys():
        total += dic[i]['preço']*dic[i]['quantidade']
      print (f"""O Saldo total em estoque é de: R$ {total}

             """)

#Função para cálculo do valor de estoque de um determinado produto
def valor_estoque_produto():

  escolha = input("""Escolha o método de escolha:

  1- Código
  2- Nome

  """)
  if escolha == '1':
    cod = input('Informe o código do produto a ser atualizado: ')
    if cod in dic:
      print (f"""Valor de {dic[cod]['nome']} em estoque é: R$ {dic[cod]['preço']*dic[cod]['quantidade']}

               """)
    else:
      print ("""Produto não encontrado

        """)

  elif escolha == '2':
    nome = input('Informe o nome do produto a ser atualizado: ')
    for k,v in dic.items():
      if v['nome']==nome:
        print (f"""Valor de {dic[k]['nome']} em estoque é: R$ {dic[k]['preço']*dic[k]['quantidade']}

                                                               """)


while entrada != '8':
  entrada = input("""Escolha uma das opções (1,2,3,4,5,6,7,8):
  1- Cadastrar item
  2- Atualizar Item
  3- Consultar Item
  4- Listar todos os itens
  5- Remover item
  6- Valor total em estoque
  7- Valor em estoque de um produto específico
  8- Finalizar programa

  """)


  match entrada:
    case '1':
      cadastrar_item()


    case '2':
      atualizar_item()

    case '3':
      consultar_item()

    case '4':
      listar_todos()

    case '5':
      remover_item()

    case '6':
      valor_total_estoque()

    case '7':
      valor_estoque_produto()


print('Programa finalizado!')