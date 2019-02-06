filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f_obj:
            print(f_obj.read())
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
