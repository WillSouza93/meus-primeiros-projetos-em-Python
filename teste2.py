#Teste de Lógica - Desafio 2
''' Nosso time de futebol terminou o campeonato. O resultado de cada correspondência é semelhante a "x: y". Os resultados de todas as partidas são registrados na coleção.
 
Por exemplo: [" 3: 1 "," 2: 2 "," 0: 1 ", ...]
 
Escreva uma função que leve essa arrecadação e conte os pontos da nossa equipe no campeonato. Regras para contagem de pontos para cada partida:
 
- se x> y - 3 pontos
- se x <y - 0 ponto
- se x = y - 1 ponto
 
Notas:
 
- há 10 partidas no campeonato
- 0 <= x <= 4
- 0 <= y <= 4 '''

#Importando modulo para gerar um placar aleatório
import random

#Criando uma lista para armazenar os nomes das equipes
times = ["SolFácil", "Pé de pano"]
#Variável que vai armazenar a pontuação de cada rodada da equipe SolFácil 
pontos_tabela = 0

print("Resultado das partidas:\n\n",times[0]," x ",times[1])
#Loop para simular 5 partidas de cada equipe, totalizando 10
for a in range(5):
    #Gerando placar aleatório
    partidas = [random.randint(0, 7), random.randint(0, 7)]
    #Comparando os resultados das partidas
    if partidas[0] > partidas[1]:
        pontos_tabela += 3
    elif partidas[0] == partidas[1]:
        pontos_tabela += 1
    #Exibindo resultados das partidas
    print("       ",partidas)
#Variável que vai armazenar a pontuação ao fim do campeonato
final = pontos_tabela
#Exibindo pontuação final da equipe SolFácil
print("\nPontuação final do time ",times[0], " é ", final)
#Fim