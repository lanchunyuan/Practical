ingredient = ''
indredients = []
# while ingredient != 'quit':
#     ingredient = input("Please input a ingredient:")
#     print(f"We can add {ingredient} in pizza.")
#     indredients.append(ingredient)
# print(indredients)

while True:
    ingredient = input("Please input a ingredient:")
    print(f"We can add {ingredient} in pizza.")
    if ingredient == 'quit':
        break
    else:
        indredients.append(ingredient)
print(indredients)