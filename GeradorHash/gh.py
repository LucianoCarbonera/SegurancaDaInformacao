import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = input(""" ### MENU - ESOLHA O TIPO DE HASH ###
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512
            Digite o número do hash de sua escolha:  """)

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(f"O hash da string é: {resultado.hexdigest()}")

elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(f"O hash da string é: {resultado.hexdigest()}")

elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(f"O hash da string é: {resultado.hexdigest()}")

elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(f"O hash da string é: {resultado.hexdigest()}")

else:
    print("Voce selecionou uma opção inválida, tente novamente")

