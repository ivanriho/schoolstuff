#kommentarer, if, {}, kommatecken"
#ska göra en kassörs


#The menu with all the different alternatives and prices
plainPizza = int(80)
Margarita = plainPizza + 20
Kebabpizza = plainPizza + 60
Vesuvio = plainPizza + 40
Menu = [Margarita, Kebabpizza, Vesuvio]

# Welcomes and asks for which pizza you'd like
print("Välkommen till våran resturang")
order = input("Vad skulle du vela beställa? ").casefold()



# Saying good choice and asking when you'd want it
# cookingTime will the be time varible that later will be used to display the time in the string
    print("Bra val")
    cookingTime = input("Om hur lång tid vill du ha den? ")
    print("Perfekt det passar oss båda, då kommer den om", cookingTime, "min")

    # Add-ons that both Margarita and Vesuvio can use, it'll ask you, depening on the choice sås will be offered as an alternative 

    ost = int(10)
    oliver = int(15)
    banan = int(25)
    svamp = int(17)

    sås = int(12)
    
# Depending on the pizza, the output will choose between the text without Sauce and the one with Sauce 

if order == "Vesuvio":
    extra =input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. För denna har vi även sås! ")
elif order == "Margarita":
    extra = input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. ")


totalSum = Margarita

#Will add the price of the add-ons to the pizzas total price, instead of using specific words to enter add on you can write anything you'd like 
#Because it searches for the word inside!

if "ost" in extra:
    totalSum += ost

if "oliver" in extra:
    totalSum += oliver

if "banan" in extra:
    totalSum += banan

if "svamp" in extra:
    totalSum += svamp

#Announcing the price 

print(f"Priset blir", totalSum, "kr, med din order som var en", order, "med", extra,)

