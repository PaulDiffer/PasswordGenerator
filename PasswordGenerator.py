import random
chars = '!"#$%&()*+,-./0123456789?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
password = ""

lengthPW = int(input("¿De que longitud quieres el password? "))

for _ in range(lengthPW):
    password += random.choice(chars)
    
print(password)