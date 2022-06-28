#Projeto - Chute um número
'''
Escreva um programa que, ao iniciar, gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até acertar o valor gerado.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

1. Quais são os dados de entrada necessários?
  * Um número de 1 a 10 gerado automaticamente;
  * Um chute do usuário.
2. O que devo fazer com estes dados?
  * Comparar o chute do usuário com o valor aleatório gerado no início do programa e informar se foi acima, abaixo ou igual.
3. Quais são as restrições deste problema?
  * Um valor aleatório de 1 a 10.
4. Qual é o resultado esperado?
  * O resultado esperado é que o programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
5. QUal é a sequência de passos a ser feitas para chegar ao resultado esperado?
  *input valor_aleatorio de 1 a 10
  input chute
  if chute > valor_aleatorio
    print "chute foi maior que o valor gerado"
  if chute < valor_aleatorio
    print "chute foi menor que o valor gerado"
  if chute = valor_aleatorio
    print "Você acertou!!!"
'''

import random

valor_aleatorio = [random.randint(1, 10)]
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleatorio[0]:
        print('O chute foi maior que o valor gerado!')
    elif chute < valor_aleatorio[0]:
        print('O chute foi menor que o valor gerado!')
    elif chute == valor_aleatorio[0]:
        acertou = True
        print('Acertô miserávi! =B')
