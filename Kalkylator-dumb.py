

num1 =float(input("Ange första numret "))

operator = input("Välj räknesätt, +,-,/,*")

num2 =float(input("Ange andra numret "))



#Additon
if operator == "+":
    print(f"Svaret blir", num1 + num2)

#Subraktion
elif operator == "-":
    print(f"Svaret blir", num1 - num2)

#Division
elif operator == "/":
    print(f"Svaret blir", num1 / num2)

#Multiplikation
elif operator == "*":
    print(f"Svaret blir", num1 * num2)