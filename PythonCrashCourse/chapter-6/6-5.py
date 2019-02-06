rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }
for river , country in rivers.items():
    print(f'{river.title()} run throuth {country}')

print('\nRivers:')
for river in rivers.keys():
    print(f'- {river}')

print('\nCountrys:')
for country in rivers.values():
    print(f'- {country}')