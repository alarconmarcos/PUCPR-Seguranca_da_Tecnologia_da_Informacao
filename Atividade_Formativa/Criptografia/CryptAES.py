# É necessário instalar o pacote pycryptodome (!pip install pycryptodome)
from base64 import b64encode, b64decode
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time


def encrypt(plain_text, key):

    salt = get_random_bytes(AES.block_size)

    private_key = hashlib.scrypt(
        key.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    cipher_config = AES.new(private_key, AES.MODE_GCM)

    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }


def decrypt(enc_dict, key):
    salt = b64decode(enc_dict['salt'])
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    private_key = hashlib.scrypt(key.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

    return decrypted


key = input("Forneça um valor de chave: ")

inicio = time.time()

print('\nIniciando o processo de criptografia AES às', time.strftime("%H:%M:%S", time.localtime()))

encrypted = encrypt("Vamos ajudar o banco de Toquio!!", key)
print('\nMensagem Cifrada: ',encrypted)

decrypted = decrypt(encrypted, key)
print('\nMensagem Decifrada:',bytes.decode(decrypted))

fim = time.time()
benchmark = fim - inicio

print('\nFinalizado o processo de criptografia AES às', time.strftime("%H:%M:%S", time.localtime()))
print('\nTempo total de processamento: ',benchmark,  'segundos')
