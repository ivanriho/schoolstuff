#kommentarer, if, {}, kommatecken"
#ska göra en kassörs
import time

# The menu with all the different alternatives and prices
plainPizza = int(80)
Margarita = plainPizza + 20
Vesuvio = plainPizza + 40
Menu = [Margarita, Vesuvio]

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

if order == "vesuvio":
    extra =input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. För denna har vi även sås! ")
elif order == "margarita":
    extra = input("Vill du ha nån annan topping på, vi har ost, oliver, banan och svamp. ")

print("Tack för din beställning, vi kommer att börja laga den nu, ge oss några sekunder att sätta in ordern")

time.sleep(5)

if order == "vesuvio":
    totalSum = Vesuvio
else: 
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

if "sås" in extra:
    totalSum += sås

# Adding the drinking questions now

cola = int(20)
sprite = int(15)
fanta = int(25)


drinks = input("Vill du ha nått att dricka till? Vi har cola, fanta och sprite. ")

if "cola" in drinks:
    totalSum += cola
if "fanta" in drinks:
    totalSum += fanta
if "sprite" in drinks:
    totalSum += sprite


#Announcing the price 
# Setting tip variable

x = int(40)
print(f"Priset blir", totalSum, "kr exlusive dricks, med din order som var en", order, "med", drinks,)

answer = input("Vill du ge dricks till lilla mig?")

if "nej" in answer:
    print("Fahhh ig vro")

elif "ja" in answer:
    print("tack så mycket")

    resultat = input("Hur mycket merci ")
    resultat = int(resultat)

    if resultat >= 40:
        print("Tack så mycket för att du dricksar med dina stora", resultat, "spänn")

    elif resultat < 40:
        print("Det är väl omtanken som räknas ig, tack för dina", resultat, "spänn")