import random

i = random.randint(0,100)
print ("Die Zufallszahl ist: ",i)

i2 = random.randint(0,100)
print ("Die Zufallszahl ist: ",i2)

if i < i2 and i < 50:
    print ("Zahl 1 ist kleiner als Zahl 2 und Mini")

elif i < 30 or i2 < 30:
    print ("Eine der beiden ist kleiner als 30")

elif i < 50 and i2 != 50:
    print ("Erste Zahl klein, zweite keine 50iger")