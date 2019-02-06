file_name = 'learning_python.txt'

with open(file_name) as f_obj:
    lines  = f_obj.readlines()

for line in lines:
    message = line.replace('Python','C')
    print(message)