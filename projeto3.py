#Projeto - Medidor de velocidade
'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua, crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima, o programa deve exibir "Não houve infrações", se estiver até 10km acima, deve exibir "Infração leve", se estiver entre 11km a 20km acima, deve exibir "Infração grave" e se estiver acima de 20km acima da velocidade, deve exibir "Infração gravíssima".
'''
velocidade_maxima = 80
velocidade_condutor = int(input('\nDigite a velocidade em que o condutor do veículo estava: '))
if velocidade_condutor <= velocidade_maxima:
  print('Não houve infrações!')
elif velocidade_condutor > velocidade_maxima and velocidade_condutor <= velocidade_maxima + 10:
  print('Infração Leve!')
elif velocidade_condutor >= velocidade_maxima + 11 and velocidade_condutor <= velocidade_maxima + 20:
  print('Infração grave')
elif velocidade_condutor > velocidade_maxima + 20:
  print('Infração gravíssima')