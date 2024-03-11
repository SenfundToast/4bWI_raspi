import random

anzahlanWürfe = 6

while True:
    print("Du hast 6 Würfe, wähle eine Zahl aus:\n")
    print("1. mach einen Wurf")
    print("2. Sehe wie viele Würfe du noch hast")
    print("3. Spiel Beenden") 

    
    selection = int(input("gibt eine Zahl ein: "))
   
    
    if selection == 1: 
        i = random.randint(1,6)
        print ("Die Zahl ist: ",i)
        anzahlanWürfe -= 1

    if selection == 2:
        print("Anzahl an Würfen derzeit: ", anzahlanWürfe)

    if selection == 3:
        print("Auf Wiedersehen")
        break

    else:
        print("Bitte geben Sie eine Zahl von 1 bis 3")