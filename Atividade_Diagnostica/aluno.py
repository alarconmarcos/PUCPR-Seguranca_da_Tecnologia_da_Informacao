# 3. Implemente um algoritmo em Python para manipular o sistema de cadastro de um aluno. 

# especificação: 

# o) Utilize uma estrutura lista para adicionar os dados dos alunos (nome, sobrenome e e-mail); 
# p) Crie uma estrutura dicionário para armazenar os dados de cada aluno associado a uma chave (matrícula); 
# q) Cadastre cinco alunos no sistema; 
# r) Imprima os dados de todos dos alunos e sua matrícula. 
 
# Exemplo de entrada: 

# * Adicione um valor para matrícula: 123456; 
# * Adicione um valor para nome: Maria; 
# * Adicione um valor para sobrenome: Silva; 
# * Adicione um valor para e-mail: maria.silva@gmail.com; 

alunos = {}

for i in range(5):
  matricula = input('Informe a matrícula: ')
  nome = input('Informe o nome: ')
  sobrenome = input('Infomre o sobrenome: ')
  email = input('Informe o e-mail: ')

  alunos[matricula] = ([nome, sobrenome, email])

for matricula in alunos:  
  aluno = alunos[matricula]
  print(f'matrícula: {matricula}, Nome Completo: {aluno[0]} {aluno[1]}, e-mail: {aluno[2]}')