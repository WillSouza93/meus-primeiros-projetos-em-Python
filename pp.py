bandas = []

while True:
  op = int(input("\n1. Adicionar banda\n2. Exibir bandas favoritas\n3. Tamanho da lista\n4. Alterar nome da banda\n5. Sair\n"))

  if (op==1):
    banda = input("Digite o nome da banda: ")
    bandas.append(banda)
  if (op==2):
    print(bandas)
  if (op==3):
    print("Tamanho da lista: ", len(bandas))
  if (op==4):
    index = int(input("Indice da banda que quer alterar: "))
    if(index<len(bandas)):
      temp = input("Nome da banda: ")
      bandas[index] = temp
    else:
      print("Banda não encontrada!")
  if (op==5):
    exit(0)