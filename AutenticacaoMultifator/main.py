'''Pontifícia Universidade Católica do Paraná

Disciplina: Segurança da Tecnologia da Informação (Turma 01)

Professor-Tutor: Wellington Rodrigo Monteiro

Alunos: BÁRBARA DE PAULA E SILVA
        DAVI RAMON GONÇALVES
        MARCOS ALARCON

Atividade: Atividade Somativa 1

Título: Desafio Autenticação e Controle de Acesso no banco de Tóquio'''


import Autentica

while True:
    print("1 - Cadastrar Usuário")
    print("2 - Verificar Email")
    print("3 - Autenticar Usuário")
    print("4 - Sair\n")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        Autentica.cadastrar()

    elif opcao == "2":
        Autentica.verificar_email()

    elif opcao == "3":
        Autentica.autenticar()

    elif opcao == "4":
        break