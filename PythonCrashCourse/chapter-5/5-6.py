age = int(input('How old is your son?'))
if age < 2:
    print('He is a infant')
elif age < 4:
    print('He is a kid.')
elif age < 13:
    print('He is a child.')
elif age < 20:
    print('He is a youth.')
elif age < 65:
    print('He is a adult')
else:
    print('He is old.')