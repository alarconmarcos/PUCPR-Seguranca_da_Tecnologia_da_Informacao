import datetime
import os
import stat


def executarcontroleacesso(usuario):
  
    try:
        arquivo = open("acesso.txt", "x")
        arquivo.write("Usuário: " + usuario + " - Data: " + str(datetime.datetime.now()) + "\n")
        arquivo.close()
        os.chmod("acesso.txt", stat.S_IROTH) # Permissão de leitura para todos
        print("\nAs Informações de acesso foram registradas com sucesso!\n")
    
    except FileExistsError:
        os.chmod("acesso.txt", stat.S_IRWXU) # Permissão de leitura, escrita e execução para o dono do arquivo
        arquivo = open("acesso.txt", "a")
        arquivo.write("\nUsuário: " + usuario + " - Data: " + str(datetime.datetime.now()))
        arquivo.close()
        os.chmod("acesso.txt", stat.S_IROTH) # Permissão de leitura para todos
        print("\nAs Informações de acesso foram registradas com sucesso!\n") 
