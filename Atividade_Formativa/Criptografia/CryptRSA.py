# É necessário instalar o pacote pycryptodome (!pip install pycryptodome)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

inicio = time.time()

TamanhoChave = 2048

print('Iniciando o processo de criptografia RSA com chave de', TamanhoChave, 'bits às', time.strftime("%H:%M:%S", time.localtime()))

keyPair = RSA.generate(TamanhoChave)

pubKey = keyPair.publickey()
print(f'Chave Pública:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})\n')
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f'Chave Privada: (n={hex(pubKey.n)}, d={hex(keyPair.d)})\n')
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

msg = b'Vamos ajudar o banco de Toquio!!'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print('\nMensagem Cifrada:', binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('\nMensagem Decifrada:', decrypted)


fim = time.time()
benchmark = fim - inicio

print('\nProcesso de criptografia RSA com chave de', TamanhoChave, 'bits finalizado às', time.strftime("%H:%M:%S", time.localtime()))
print('\nTempo total de processamento: ',benchmark,  ' segundos')
