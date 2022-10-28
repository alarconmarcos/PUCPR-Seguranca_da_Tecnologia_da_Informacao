# 1. Implemente um algoritmo em Python para manipular sua lista de filmes favoritos. 

# Especificação: 

# a) Crie uma lista vazia em Python; 
# b)Adicione o nome de 5 filmes na lista de favoritos; 
# c) O usuário deverá solicitar o nome de cada filme (usar o comando while); 
# d) Posteriormente imprima todos os filmes e sua posição na lista; 
# f) Para imprimir a lista utilizar o comando for e conjunto da função enumerate(). 

lista_filmes = []

while len(lista_filmes) < 5:
  filme = input('Informe o nome de um filme: ')
  lista_filmes.append(filme)
  
for posicao, filme in enumerate(lista_filmes, 1):
  print(f'Posição: {posicao}: Filme: {filme}')
