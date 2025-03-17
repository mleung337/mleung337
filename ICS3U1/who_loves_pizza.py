# Matthew Leung

pizza_names = ['hawaiian pizza', "meat lover's pizza", 'vegetarian pizza']

for pizza in pizza_names:
    print('I like {}.'.format(pizza))

print('Pizza is great.\n')
friend_pizzas = list(pizza_names)
pizza_names.append('three cheese pizza')
friend_pizzas.append('vegan pizza')

for pizza in pizza_names:
    print('My favourite pizzas are {}.'.format(pizza))

print('\n')

for friend_pizza in friend_pizzas:
    print("My friend's favourite pizzas are {}.".format(friend_pizza))
