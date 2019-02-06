filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat is your name?")
    if name == 'quit':
        break
    else:
        with open(filename,'a') as f_obj:
            f_obj.write(f'{name}\n')
            print("Hi " + name + ", you've been added to the guest book.")



