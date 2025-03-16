# Matthew Leung

amount_of_bread = 2 
amount_of_cheese = 3

price_of_bread = int(input("What is the current price for a loaf of bread? "))
print("The price for a loaf of bread is", price_of_bread)
price_of_cheese= int(input("What is the current price for a block of cheese? "))
print("The price for a block of cheese is", price_of_cheese)

total_price = amount_of_bread * price_of_bread + amount_of_cheese * price_of_cheese
print("The price for", amount_of_bread, "loaves of bread and", amount_of_cheese, "blocks of cheese is", total_price)
