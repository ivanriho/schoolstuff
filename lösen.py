#Ska vara aktiv loop lösen

password = ""
while password != "Banan":
    password = input("Snälla ange lösen")
    if password == "Apple":
        print("Du hade rätt")
        break
    elif password == "kebab":
        print("Du hade fel, försök igen")