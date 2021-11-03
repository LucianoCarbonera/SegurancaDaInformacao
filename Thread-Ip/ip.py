import ipaddress

#ip = '192.168.0.1'
rede_ip = '192.168.0.0/24'

#endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(rede_ip)

#print(ip + 100)

for ip in rede:
    print(ip)
