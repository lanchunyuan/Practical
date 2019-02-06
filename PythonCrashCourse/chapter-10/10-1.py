print("--- Reading in the entire file:")
with open('learning_python.txt','r') as f_obj:
    contents = f_obj.read()
    print(contents)

print("\n--- Looping over the lines:")
with open('learning_python.txt','r') as f_obj:
    for line in f_obj:
        print(line.strip())

print("\n--- Storing the lines in a list:")
with open('learning_python.txt') as f_obj:
    lines = f_obj.readlines()

for line in lines:
    print(line.strip())
