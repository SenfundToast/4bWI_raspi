import random

i = random.randint(0,100)
print ("Die Zufallszahl ist: ",i)

if i <=20 :
    print ("Mini")
elif i >= 20 and i <=50: print("Medium")

else:
    print("Large")