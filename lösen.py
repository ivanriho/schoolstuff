#Ska vara aktiv loop lösen

password = "" # Gör att variabeln förblir odefinerad
while password != "Banan": #Loopen kör tills lösenordet inte är banan
    password = input("Snälla ange lösen")
    if password == "Apple":
        print("Du hade rätt")
        break
    elif password == "kebab":
        print("Du hade fel, försök igen")