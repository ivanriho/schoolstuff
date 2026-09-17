#kommentarer, if, {}, kommatecken"
#ska göra en kassörs

plainPizza = int(80)
Margarita = plainPizza + 20
Kebabpizza = plainPizza + 60
Vesuvio = plainPizza + 40
Menu = [Margarita, Kebabpizza, Vesuvio]

print("Välkommen till våran resturang")
order = input("Vad skulle du vela beställa? ").casefold()


# om pizza sort inte finns så ska man inte kunna gå vidare



if order == "Margarita, Kebabpizza, Vesuvio":



    print("Bra val")
    cookingTime = input("Om hur lång tid vill du ha den? ")
    print("Perfekt det passar oss båda, då kommer den om", cookingTime, "min")

    #Extra tillägg som finns på margarita


    ost = int(10)
    oliver = int(15)
    banan = int(25)
    svamp = int(17)

    sås = int(12)
    

if order == "Vesuvio":
    extra =input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. För denna har vi även sås! ")
elif order == "Margarita":
    extra = input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. ")


totalSum = Margarita


if "ost" in extra:
    totalSum += ost

if "oliver" in extra:
    totalSum += oliver

if "banan" in extra:
    totalSum += banan

if "svamp" in extra:
    totalSum += svamp

print(f"Priset blir", totalSum, "kr, med din order som var en", order, "med", extra,)

