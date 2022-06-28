#Coleções(listas)
'''
preco_1 = 20
preco_2 = 50
preco_3 = 100

#lista
precos = [20,50,100]
#          0, 1,  2
print(precos[0])
print(precos.index(200))

diversidades = [27,'Willian', True]
print(diversidade[0])
print(diversidade[1])
print(diversidade[2])

#Laços em iteráveis
for preco in precos:
  print(preco)
'''

#Problema - Some as idades
#A partir de uma coleção de dados "idades" [15, 46, 75, 34, 23], imprima na tela a soma destes valores
'''
idades = [15, 46, 75, 34, 23]
total = 0
loop idade in idades
  total = total + idade
print total
'''

idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
  total = total + idade
print(total)