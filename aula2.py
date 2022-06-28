#condicionais
#if, elif e else
# Encontre o maior entre dois números
'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
  print O primeiro número é maior!
elif primeiro_valor < segundo_valor
  print O segundo número é maior!
else
  print Os números são iguais!
'''

primeiro_valor = input('Digite o primeiro número: ')
segundo_valor = input('Digite o segundo número: ')

if int(primeiro_valor) > int(segundo_valor):
  print('O primeiro número é maior!')
elif int(primeiro_valor) < int(segundo_valor):
  print('O segundo número é maior!')
else:
  print('Os números são iguais!!!')