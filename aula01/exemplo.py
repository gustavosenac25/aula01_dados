# # #tipos de variaveis que servem como atributos: string, inteira, float
# # nome = 'Ana'
# # idade = 25
# # salario = 15000.0

# # #novas funcoes f e para juntar um texto com a variavel, \n e para mudar de linha, {} e para colocar variavel
# # print(f'O nome dela é {nome}, \nela tem {idade} anos \ne recebe {salario} reais mensais')

# # #a variavel recebe a ultima atribuicao x=20, embora ja tenha sido 5 anteriormente:
# # x = 5
# # x = 20
# # print(x)

# nome = input('Digite o nome: ')
# print(f'Olá, {nome}!!')

# cor = input('Qual sua cor favorita? ')
# print(f'Que coincidência! Eu também adoro {cor}!')

# trote = input('Quem é? ')
# print(f'O meu também é {trote}!')

# n1 = 5
# n2 = 3
# soma = n1 + n2
# subtracao = n1 - n2
# divisao = n1 / n2
# print(f'Entre os dois números a soma foi {soma}, a subtração foi {subtracao} e a divisão foi {divisao}')

#int na frente de imput de texto, faz com que um número que antes era texto (string), tenha valor numerico (inteiro). também pode usar o comando que transforma em variavel tipo decimal (float)
#numeros tipo string nao dao para fazer certas operacoes aritimeticas, como multiplicacao e divisao.
# n1 = int(input('Em que ano você nasceu? '))
# n2 = int(input ('Em que ano seu pai nasceu? '))
# idade = 2025 - n1
# idadepai = 2025 - n2
# diferenca = n1 - n2
# print(f'Então vocé tem {idade} anos, seu pai tem {idadepai} anos e você nasceu quando ele tinha {diferenca} anos')

# nome_usuario = input('Informe seu nome: ')
# idade_usuario = input('Informe sua idade: ')
# print(f'O nome delu é {nome_usuario} e elu tem {idade_usuario} anos')

# nome = input('Diga o seu nome: ')
# cidade = input('e a cidade de onde está falando: ')
# print(f'Chamada a cobrar, para aceitar continue na linha após a identificação: Oi, sou {nome} de {cidade}!')

# idade = int(input('Qual é sua idade? '))
# ano_nascimento = 2025 - idade
# print(f'Então você deve ter nascido em {ano_nascimento}.')
# print(input('Verdade?! '))

# monto = float(input('Quanto você conseguiu arrecadar de grana? '))
# ingresso = 25
# quantidade = int(monto / ingresso)
# resto = monto % ingresso
# print(f'Com esse valor você pode comprar {quantidade} ingressos \nSeu troco será {resto}')

# preco = float(input('Qual o valor do kilo? '))
# qnt = float(input('Quantos kilos você quer comprar? '))
# total = preco * qnt
# valor_final = total - (total * 0.1)
# print(f'O valor a ser pago, com 10% de desconto é {valor_final} reais')

# salario = float(input('Qual é o salário do funcionário? '))
# aumento = float(input('Qual é a porcentágem do aumento que ele vai receber? '))
# salario_final = salario + (salario * aumento / 100)
# print(f'Com esse aumento, o salário final dele será {salario_final} reais')


