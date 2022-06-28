#Exemplo 5 - Fatorial de um número
'''
Crie um programa que recebe um número e imprime o seu fatorial.

# Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra:
(tente explicar o problema para você mesmo em voz alta e peça mais informações/ investigue mais até compreender completamente)

1. Quais são os dados de entrada necessários?
  * Um número.
2. O que devo fazer com estes dados?
  * Calcular o seu fatorial e exibir na tela.
3. Quais são as restrições deste problema?
  * O número deve ser positivo;
  * O número deve ser do tipo Inteiro.
4. Qual é o resultado esperado?
  * O resultado esperado é que o fatorial do número inserido seja calculado e exibido na tela.
5. QUal é a sequência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
  fatorial = fatorial * numero
print fatorial
'''

numero = int(input('Digite um número: '))
if numero > 0:
  fatorial = 1
  for item in range(1,numero +1):
    fatorial = fatorial * item
  print(fatorial)
elif numero <= 0:
  print('Número inválido')