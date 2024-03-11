geld = 0

while True:
    print("\nSelektieren Sie die gewünschter Funktion: \n")
    print("1. Einzahlen") 
    print("2. Abheben") 
    print("3. Kontostand") 
    print("4. Programm Beenden") 

    selection = int(input('\nGeben sie die Zahl ein: '))

    if selection == 1:
        einzahlung = float(input("Geben sie an wie viel sie einzahlen möchten: "))
        geld += einzahlung
        print("Erfolgreich eingezahlt: ", geld)

    if selection == 2:
        auszahlung = float(input("Geben sie an wie viel sie auszahlen möchten: "))
        geld -= auszahlung
        print("Erfolgreich ausgezahlt: ", geld)

    if selection == 3:
        print("\nDerzeitiger Kontostand: ", geld)
    
    if selection == 4:
        print("Auf wiedersehen")
        break

    else:
        print("Bitte geben sie eine Zahl von 1 bis 4")