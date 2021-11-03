import hashlib

arq1 = 'a.txt'
arq2 = 'b.txt'

hash1 = hashlib.new('ripemd160')  #

hash1.update(open(arq1, 'rb').read())  #rb abertura em modo binário

hash2 = hashlib.new('ripemd160')

hash2.update(open(arq2, 'rb').read())  #rb abertura em modo binário

#função digest resume dados passado pelo update, se o
if hash1.digest() != hash2.digest():
    print(f'o arquivo: {arq1} é diferente do arquivo: {arq2}')
    print('Hash do arquivo a.xt: ', hash1.hexdigest())
    print('Hash do arquivo b.xt: ', hash2.hexdigest())
else:
    print(f'o arquivo: {arq1} é igual ao arquivo: {arq2}')
    print('Hash: ', hash2.hexdigest())


