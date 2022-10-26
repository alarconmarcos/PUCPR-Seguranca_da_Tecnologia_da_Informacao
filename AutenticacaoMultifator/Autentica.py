import pyrebase
import random
import Email

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

def cadastrar():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")
    status = auth.create_user_with_email_and_password(user,password)
    if status['idToken']:
        print("Usuário:", user+" cadastrado com sucesso!\n")


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

    if verifyEmail:
        print("Autenticação em dois fatores\n")
        codigo = random.randint(100, 1000)

        Email.enviar_email(codigo)

        codigoEmail = int(input("Entre com o código que foi enviado paro o seu e-mail: "))

        if codigo == codigoEmail:
            print("Usuário Autenticado com Sucesso!!!\n")
        else:
            print("Código Inválido!!\n")
    else:
        print("E-mail não verificado!\n")

def verificar_email():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha: ")
    status = auth.sign_in_with_email_and_password(user, password)
    idToken = status["idToken"]
    auth.send_email_verification(idToken)
    print("Email de verificação enviado para: ", user+"\n")