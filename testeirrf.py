salario_bruto = float(input("Digite o valor bruto do salário: "))

if salario_bruto <= 1903.98:
  print("O contribuinte está isento")
elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
  aliquota_1 = 7.5 / 100
  taxa_1 = 142.80
  desconto = (salario_bruto * aliquota_1) - taxa_1
  print('O valor da parcela é de: R$ ' + str(desconto))
  salario_liquido = salario_bruto - desconto
  print('O valor do salário já com desconto é: R$ ' + str(salario_liquido))
elif salario_bruto >2826.65 and salario_bruto <= 3751.05:
  aliquota_2 = 15.0 / 100
  taxa_2 = 354.80
  desconto = (salario_bruto * aliquota_2) - taxa_2
  print('O valor da parcela é de: R$ ' + str(desconto))
  salario_liquido = salario_bruto - desconto
  print('O valor do salário já com desconto é: R$ ' + str(salario_liquido))
elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
  aliquota_3 = 22.5 / 100
  taxa_3 = 636.13
  desconto = (salario_bruto * aliquota_3) - taxa_3
  print('O valor da parcela é de: R$ ' + str(desconto))
  salario_liquido = salario_bruto - desconto
  print('O valor do salário já com desconto é: R$ ' + str(salario_liquido))
elif salario_bruto > 4664.68:
  aliquota_4 = 27.5 / 100
  taxa_4 = 869.36
  desconto = (salario_bruto * aliquota_4) - taxa_4
  print('O valor da parcela é de: R$ ' + str(desconto))
  salario_liquido = salario_bruto - desconto
  print('O valor do salário já com desconto é: R$ ' + str(salario_liquido))