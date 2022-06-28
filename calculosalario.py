#Variáveis
salario_inicial = float(input("Digite o valor do salário: "))

while True:
  #Comparação: Se salario_inicial for menor < ou igual = a 500
  if salario_inicial <= 500:
    reajuste20 = 20.0 / 100.0
    salario_final = salario_inicial + (reajuste20 * salario_inicial)
    #imprima
    print("Reajuste de 20%.\nNovo salário é: ", salario_final)
  #Se salario_inicial for maior > que 500
  elif salario_inicial > 500:
    reajuste10 = 10.0 / 100.0
    salario_final = salario_inicial + (reajuste10 * salario_inicial)
    #imprima
    print("Reajuste de 10%.\nNovo salário é: ", salario_final)

