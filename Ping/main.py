import os  #biblioteca os integra programas e recursos do S.O
import time

#=------------------------------- PING SIMPLES -----------------------------------------
"""
print("#" * 60)
ip_ou_host = input("IP ou Host a ser verificado: ")
print("-" * 60)
os.system(f'ping -n 6 {ip_ou_host}')
print("-" * 60)
"""
#=------------------------------- PING MULTIPLO -----------------------------------------
with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(f"Verificando ip: {ip}")
        print("-" * 60)
        os.system(f'ping -n 6 {ip}')
        print("-" * 60)
        time.sleep(5)