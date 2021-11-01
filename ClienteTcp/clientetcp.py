import socket
import sys

def main():
    try:
        # socket.AF_INET (IP),  socket.SOCK_STREAM (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print(e)
        sys.exit()

    print("Socket criado com sucesso")

    host_alvo = input("Digite o host ou ip: ")
    porta_alvo = input("Digite a porta: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f"Cliente TCP Conectado com Sucesso no host {host_alvo} porta {porta_alvo}")
        s.shutdown(2)
    except socket.error as e:
        print(f"Não foi possivel conectar host {host_alvo} porta {porta_alvo}")
        print(e)
        sys.exit()

if __name__ == "__main__":
    main()
