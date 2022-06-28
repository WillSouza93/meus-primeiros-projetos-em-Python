'''# Teste de Lógica - Desafio 1
 
O primeiro século vai do ano 1 até e incluindo o ano 100, o segundo século - do ano 101 até e incluindo * o ano 200, etc.
 
Dado um ano, retorne o século em que ele se encontra.
 
Exemplos:
 
entrada: 1705, resultado: 18
entrada: 1900, resultado: 19
entrada: 1601, resultado: 17
entrada: 2000, resultado: 20
'''
#Declarando variável que vai receber a data do usuário
ano = int(input('Digite um ano entre 1 e 2022: '))

#criando as condicionais para exibir o resultado para o usuário
if ano <1 or ano >2022:
  print('Ano incorreto')
elif ano >=1 and ano <=100:
  print('Este ano é referente ao século: 1')
elif ano >=101 and ano <=200:
  print('Este ano é referente ao século: 2')
elif ano >=201 and ano <=300:
  print('Este ano é referente ao século: 3')
elif ano >=301 and ano <=400:
  print('Este ano é referente ao século: 4')
elif ano >=401 and ano <=500:
  print('Este ano é referente ao século: 5')
elif ano >=501 and ano <=600:
  print('Este ano é referente ao século: 6')
elif ano >=601 and ano <=700:
  print('Este ano é referente ao século: 7')
elif ano >=701 and ano <=800:
  print('Este ano é referente ao século: 8')
elif ano >=801 and ano <=900:
  print('Este ano é referente ao século: 9')
elif ano >=901 and ano <=1000:
  print('Este ano é referente ao século: 10')
elif ano >=1001 and ano <=1100:
  print('Este ano é referente ao século: 11')
elif ano >=1101 and ano <=1200:
  print('Este ano é referente ao século: 12')
elif ano >=1201 and ano <=1300:
  print('Este ano é referente ao século: 13')
elif ano >=1301 and ano <=1400:
  print('Este ano é referente ao século: 14')
elif ano >=1401 and ano <=1500:
  print('Este ano é referente ao século: 15')
elif ano >=1501 and ano <=1600:
  print('Este ano é referente ao século: 16')
elif ano >=1601 and ano <=1700:
  print('Este ano é referente ao século: 17')
elif ano >=1701 and ano <=1800:
  print('Este ano é referente ao século: 18')
elif ano >=1801 and ano <=1900:
  print('Este ano é referente ao século: 19')
elif ano >=1901 and ano <=2000:
  print('Este ano é referente ao século: 20')
elif ano >=2001 and ano <=2022:
  print('Este ano é referente ao século: 21')
#fim