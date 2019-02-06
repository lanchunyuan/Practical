from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def rool_die(self):
        return randint(1,self.sides)

d6 = Die()
results = []

for roll_num in range(10):
    result = d6.rool_die()
    results.append(result)

print(results)

d6 = Die(sides = 10)

results = []

for roll_num in range(10):
    result = d6.rool_die()
    results.append(result)

print(results)