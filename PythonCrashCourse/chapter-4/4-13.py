menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )
for item in menu_items:
    print(item)
try:
    menu_items[0] = 'king crab legs'
except TypeError:
    menu_items = (
        'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
        'black cod tips', 'king crab legs',
    )
print(menu_items)
