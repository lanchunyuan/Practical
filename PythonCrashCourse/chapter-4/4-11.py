favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]
favorite_pizzas.append('sausage')
friend_pizzas.insert(0,'mushroom')
print('My favorite pizzas are:')
for pizza in favorite_pizzas:
    print(pizza)
print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)