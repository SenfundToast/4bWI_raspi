import random

n = 0

while True:
    i = random.randint(10,30)
    print("Zufallszahl:",i)

    if i == 15 or i == 25:
        break

    n += i 

print("Summe:", n)