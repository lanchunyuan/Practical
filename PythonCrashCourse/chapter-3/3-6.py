guests = ['Tom','Tesla','Anae']
print(guests[0] + ',Would you like to have a dinner with me?')
print(guests[1] + ',Would you like to have a dinner with me?')
print(guests[2] + ',Would you like to have a dinner with me?')
absent = guests.pop(1)
print(guests)
print(absent + " can not present.")
guests.append('Eric')
for _ in guests:
	print(_ + " would present.")
print("I found a bigger table.")
guests.insert(0,'Bob')
guests.insert(0,'Jonh')
#guests.insert(len(guests),'Leo')
guests.insert(-1,'Leo')
guests.insert(len(guests),'Ann')
print(guests)
for guest in guests:
	print(guest + ",Please come to dinner.")
