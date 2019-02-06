def collatz(number):
    if number%2 == 0:
        result = number//2
        print(result)
        return result
    elif number%2 == 1:
        result = 3*number+1
        print(result)
        return result

while True:
    try:
        number = input("Enter a number: ")
        number = int(number)
        a = collatz(number)
        if a == 1:
            break
    except ValueError:
        print("Your input is not a number!")
