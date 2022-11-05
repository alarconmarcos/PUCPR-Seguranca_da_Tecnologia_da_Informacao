import pyrebase
import random
import Email
import acesso
import re
from time import sleep

firebaseConfig = {
    "apiKey": "AIzaSyAhpYlI3dA7PQ5GKxv5FaQv0FaZs3hAS80",
    "authDomain": "fir-pucpr-4d42a.firebaseapp.com",
    "projectId": "fir-pucpr-4d42a",
    "databaseURL": "https://" + "fir-pucpr-4d42a" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-4d42a.appspot.com",
    "messagingSenderId": "454293494879",
    "appId": "1:454293494879:web:f99cb8da933fc2a5d9cfea",
    "measurementId": "G-CX58JLRCDD"
}
# função para criar um novo usuário
def cadastrar():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    user = ""
    password = ""

    # verifica se o email não esta vazio e se é um e-mail válido
    while (user == "" or check_email(user) == False):
        user = input("Digite seu e-mail válido: ")

    # verifica se a senha não está vazia se se tem possui no mínimo 6 caracteres
    while (password == "" or len(password) < 6):
        password = input("Digite sua senha com no mínimo 6 caracteres: ")

    try:
        status = auth.create_user_with_email_and_password(user,password)
        if status['idToken']:
            print("\nUsuário:", user+" cadastrado com sucesso!\n")
        else:
            print("\nErro ao cadastrar usuário!\n")
    except:
        print("\nUsuário já cadastrado!\n")


# função para logar um usuário
def autenticar():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    user = ""
    password = ""

    # verifica se o email não esta vazio e se é um e-mail válido
    while (user == "" or check_email(user) == False):
        user = input("Digite seu e-mail válido: ")

    # verifica se a senha não está vazia se se tem possui no mínimo 6 caracteres
    while (password == "" or len(password) < 6):
        password = input("Digite sua senha com no mínimo 6 caracteres: ")

    try:
        status = auth.sign_in_with_email_and_password(user, password)
        idToken = status["idToken"]
        info = auth.get_account_info(idToken)
        users = info["users"]
        verifyEmail = users[0]["emailVerified"]

        # Se o email foi verificado
        if verifyEmail:
            print("\nIniciando autenticação em dois fatores")
            codigo = random.randint(100, 1000)

            # Envia o email com o código de verificação
            Email.enviar_email(codigo, user)

            codigoEmail = int(input("\nInforme o código enviado para o seu e-mail: "))

            # Verifica em 3 tentativas se o código informado é igual ao enviado por email
            for i in range(2):
                if codigoEmail == codigo:
                    print("\nAutenticação realizada com sucesso!\n")
                    sleep(3)
                    print("\nIniciando controle de Acesso...\n")
                    sleep(3)
                    # Chama a função de controle de acesso
                    acesso.executarcontroleacesso(user)
                    break
                else:
                    print("\nCódigo incorreto, tente novamente")
                    codigoEmail = int(input("\nInforme o código enviado para o seu e-mail: "))
                    if i == 1:
                        print("\nNúmero de tentativas excedido")
                        break
        else:
            print("\nE-mail não verificado!\n")
    except:
        print("\nUsuário ou senha inválidos!\n")
        autenticar()


# função para enviar um email de verificação
def verificar_email():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    user = ""
    password = ""

    # verifica se o email não esta vazio e se é um e-mail válido
    while (user == "" or check_email(user) == False):
        user = input("Digite seu e-mail válido: ")

    # verifica se a senha não está vazia se se tem possui no mínimo 6 caracteres
    while (password == "" or len(password) < 6):
        password = input("Digite sua senha com no mínimo 6 caracteres: ")

    try:
        status = auth.sign_in_with_email_and_password(user, password)
        idToken = status["idToken"]
        auth.send_email_verification(idToken)
        print("\nEmail de verificação enviado para: ", user+"\n")
    except:
        print("\nUsuário ou senha inválidos!\n")


# função para verificar se o email é válido
def check_email(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.match(pat, email):
        return True
    else:
        print("E-mail inválido!")
        return False