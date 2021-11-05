import ctypes

caminho = input("Digite o caminho da a ser ocultado: ")
atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributeW(caminho, atributo_ocultar)

if retorno:
    print("Arquivo não foi ocultado")
else:
    print("Arquivo não foi ocultado")
