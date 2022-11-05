import datetime
import os
import stat
from time import sleep


def executarcontroleacesso(usuario):
  
    if os.path.isfile('acesso.txt'):
        # Dá Permissão de leitura, escrita e execução para o dono do arquivo
        os.chmod("acesso.txt", stat.S_IRWXU)
        print("\nAtribuindo permissão de leitura e escrita...\n")
        sleep(3)

        # Abre o arquivo para adicionar as informações de acesso
        arquivo = open("acesso.txt", "a")
        print("\nAbrindo arquivo para edição...\n")
        sleep(3)

        # Adiciona as informações de acesso
        arquivo.write("\nUsuário: " + usuario + " - Data: " + str(datetime.datetime.now()))
        print("\nRegistrando informações de acesso do usuário...\n")
        sleep(3)

    else:
        # Criar um arquivo texto pelo Python (arquivo “acesso.txt”);
        arquivo = open("acesso.txt", "x")
        print("\nAbrindo arquivo para edição...\n")
        sleep(3)

        # Adiciona as informações de acesso
        arquivo.write("Usuário: " + usuario + " - Data: " + str(datetime.datetime.now()))
        print("\nRegistrando informações de acesso do usuário...\n")
        sleep(3)

    # Fecha o arquivo
    arquivo.close()
    print("\nFechando o arquivo...\n")
    sleep(3)

    # Permissão de somente leitura
    os.chmod("acesso.txt", stat.S_IRUSR)
    print("\nDefinindo o arquivo como somente leitura...\n")
    sleep(3)

    print("\nInformações de acesso registradas com sucesso!\n")
