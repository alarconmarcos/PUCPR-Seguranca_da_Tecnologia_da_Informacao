# 2. Implemente um algoritmo em Python para manipular uma lista de material escolar. 

# Especificação: 

# f) Crie duas estruturas de dicionário:  
# g) Armazenar 3 itens escolares no primeiro dicionário; 
# h) Criar o segundo dicionário vazio; 
# i) Os itens devem ser solicitados ao usuário (usar o comando while); 
# j) Código do produto (chave do dicionário); 
# k) Tipo do material (valor do dicionário); 
# l) Permita que o usuário adicione apenas 5 elementos na lista; 
# m) Atualize o primeiro dicionário com o conteúdo do segundo (usar a função update()); 
# n) Posteriormente imprima todos os elementos da lista (usar o comando for). 

dicionario1 = {'001':'Lápis', '002':'Caneta', '003':'Caderno'}
dicionario2 = {}

while len(dicionario2) < 5:
  codigo_produto = input('Informe o código do produto: ')
  tipo_material = input('Informe o tipo do material: ')

  dicionario2[codigo_produto] = tipo_material
  print(f'Dicionário 2: {dicionario2}')

dicionario1.update(dicionario2)

for codigo in dicionario1:
  print(f'Código: {codigo}, Descrição: {dicionario1[codigo]}')