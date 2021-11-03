import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(2)
        print(f'Piloto: {piloto}, km: {trajeto} \n')


t_carro1 = Thread(target=carro, args=[1, 'Bruno Senna'])
t_carro2 = Thread(target=carro, args=[1.5, 'Hamilton'])

t_carro1.start()
t_carro2.start()
