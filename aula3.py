#Laços de repetição + Listas

#for palavra in range(1,4):
#  print('Carregando')
#
#for item in range(1,21):
#  print(item)
#
#for item in range(1,21,2):
#  print(item)
#
#nomes = ['Willian', 'Mayara', 'Manuella', 'Belo', 'Nina']
#for nome in nomes:
#  print(nome)

#Problema - Imprima os números de 1 a N
'''
valor = input numero_maximo
valor_inicial = 1
loop de valor_inicial a numero_maximo
  print valor
'''
valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1):
  print(numero)