items = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(spam):
    count =0
    print('Inventory:')
    for k,v in spam.items():
        print(str(v) + ' ' + k)
        count += v
    print('Total number of items : ' + str(count))

# displayInventory(items)


def addToInventory(inventory, addedItems):
# your code goes here

    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory


    # if the item in the dict ,update the value,or add the key and value
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
