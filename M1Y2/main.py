import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
request = int(input("Введите длину пароля:"))
password = ''

for i in range(request):
    password += random.choice(symbols)
print(password)