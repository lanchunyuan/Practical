while True:
    print('Input q to quit')
    try:
        a = input('Give me a number:')
        if a == 'q':
            break
        else:
            a = int(a)

        b = input('Give me a another number:')
        if b == 'q':
            break
        else:
            b = int(b)
    except ValueError:
        print("Sorry, I really needed a number.")
    else:
        sum  = a + b
        print(f'The sum is {sum}')

