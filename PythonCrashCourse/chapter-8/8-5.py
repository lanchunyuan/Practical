def describe_city(city,country = 'Iceland'):
    print(f'{city.title()} is in {country.title()}.')

describe_city('Reykjavik')
describe_city('beijing','china')
describe_city('New York','USA')