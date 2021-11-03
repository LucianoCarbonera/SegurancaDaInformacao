import random, string

tam = 16
chars = string.ascii_letters + string.digits + 'ç!@#$%*&'
rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(tam)))

