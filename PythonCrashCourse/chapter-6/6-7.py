# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
    }
people.append(person)

print(people)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")
