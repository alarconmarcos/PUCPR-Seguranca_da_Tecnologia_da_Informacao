import pyrebase
import random
import Email
import acesso

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

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")

    # Se a senha tiver pelo menos 6 caracteres
    if len(password) >= 6:
        status = auth.create_user_with_email_and_password(user,password)
        if status['idToken']:
            print("\nUsuário:", user+" cadastrado com sucesso!")
        else:
            print("\nErro ao cadastrar usuário!")
    else:
        print("\nSenha deve ter pelo menos 6 caracteres!")


# função para logar um usuário
def autenticar():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    user = input("Informe seu e-mail de acesso: ")
    password = input("Informe sua senha: ")
    status = auth.sign_in_with_email_and_password(user, password)
    idToken = status["idToken"]
    info = auth.get_account_info(idToken)
    users = info["users"]
    verifyEmail = users[0]["emailVerified"]

    # Se o email foi verificado
    if verifyEmail:
        print("\nAutenticação em dois fatores")
        codigo = random.randint(100, 1000)

        Email.enviar_email(codigo, user)

        codigoEmail = int(input("\nInforme o código enviado para o seu e-mail: "))

        if codigo == codigoEmail:
            print("\nUsuário Autenticado com Sucesso!!!")
            acesso.executarcontroleacesso(user)
        else:
            print("\nCódigo Inválido!!\n")
    else:
        print("\nE-mail não verificado!\n")


# função para enviar um email de verificação
def verificar_email():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha: ")
    status = auth.sign_in_with_email_and_password(user, password)
    idToken = status["idToken"]
    auth.send_email_verification(idToken)
    print("\nEmail de verificação enviado para: ", user) 