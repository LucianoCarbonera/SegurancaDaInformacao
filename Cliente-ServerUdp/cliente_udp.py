import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente socket criado com sucesso !")

host = 'localhost'
port = 5433
mensagem = input("Mensagem ao servidor: ")
mensagem = mensagem + '\n'

try:
    #print("Cliente:" + mensagem + "\n")
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f"Cliente: {dados}")

finally:
    print("Cliente: Fechando a conexão")
    s.close()

