import datetime
import os
import stat


def executarcontroleacesso(usuario):
  
    if os.path.isfile('acesso.txt'):
        # Dá Permissão de leitura, escrita e execução para o dono do arquivo
        os.chmod("acesso.txt", stat.S_IRWXU)

        # Abre o arquivo para adicionar as informações de acesso
        arquivo = open("acesso.txt", "w")

        # Adiciona as informações de acesso
        arquivo.write("\nUsuário: " + usuario + " - Data: " + str(datetime.datetime.now()))

    else:
        # Criar um arquivo texto pelo Python (arquivo “acesso.txt”);
        arquivo = open("acesso.txt", "x")

        # Adiciona as informações de acesso
        arquivo.write("Usuário: " + usuario + " - Data: " + str(datetime.datetime.now()) + "\n")

    # Fecha o arquivo
    arquivo.close()

    # Permissão de somente leitura
    os.chmod("acesso.txt", stat.S_IRUSR)

    print("\nAs Informações de acesso foram registradas com sucesso!\n")
    


