'''
Pontifícia Universidade Católica do Paraná
Disciplina: Segurança da Tecnologia da Informação
Author: Marcos Alarcon - 04/11/2022
Autenticação Função Hash Criptográfica MD5 - Desafio Banco de Tóquio
'''

import hashlib
import os

def cadastrar():
    nome = input("Informe o nome do usuário: ")
    login = input("Informe o login do usuário: ")
    senha = input("Informe a senha do usuário: ")

    if login == "" or senha == "":
        print("Login ou senha não informados\n")
    else:
        hash = hashlib.md5(senha.encode())
        senhaHash = hash.hexdigest()

        if os.path.isfile("banco.txt"):
            arquivo = open('banco.txt', 'r')
            listaUsuario = []

            for linha in arquivo:
                # Separa os valores nome, login e senha.
                usuario = linha.split(";")
                # Removendo a quebra de linha
                usuario[2] = usuario[2].replace("\n","")
                # Adicionando os usuários em uma lista
                listaUsuario.append(usuario)
            arquivo.close()

            checkUsuario = 0
            for user in listaUsuario:
                if user[1] == login:
                    checkUsuario = 1
                    break
                
             # Usuário não cadastrado
            if checkUsuario == 0:
                arquivo = open('banco.txt', 'a')
                arquivo.write(nome+";"+login+";"+senhaHash+"\n")
                arquivo.close()
            else:
                print("Usuário já cadastrado\n")
        else:
            arquivo = open('banco.txt', 'w')
            arquivo.write(nome+";"+login+";"+senhaHash+"\n")
            arquivo.close()

def autenticar():

    arquivo = open('banco.txt', 'r')
    listaUsuario = []
    # Percorrendo cada linha do arquivo
    for linha in arquivo:
        # Separa os valores nome, login e senha.
        usuario = linha.split(";")
        # Removendo a quebra de linha
        usuario[2] = usuario[2].replace("\n","")
        # Adicionando os usuários em uma lista
        listaUsuario.append(usuario)
    arquivo.close()

    loginAutenticao = input("Informe seu login: ")
    senhaAutenticao = input("Informe sua senha: ")
    hash = hashlib.md5(senhaAutenticao.encode())
    senhaHash = hash.hexdigest()

    checkUsuario = 0
    for user in listaUsuario:
        if user[1] == loginAutenticao:
            checkUsuario = 1
            if user[2] == senhaHash:
                print("Olá "+user[0]+" seja bem-vindo!!!\n")
            else:
                print("Autenticacao Invalida !!\n")

    # Usuário não cadastrado
    if checkUsuario == 0:
        print("Autenticacao Invalida !!\n")

while(True):
    print("1 - Cadastrar")
    print("2 - Autenticar")
    print("3 - Sair")
    print("")

    opcao = input("Selecione uma opcao: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        autenticar()
    elif opcao == "3":
        print("Saindo!!!\n")
        break
    else:
        print("Opção Inválida\n")
        print("")