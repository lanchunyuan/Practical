favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
    }

for name,places in favorite_places.items():
    print("\n" + f'{name.title()}\'s favorite places:')
    for place in places:
        print(f'- {place}')
