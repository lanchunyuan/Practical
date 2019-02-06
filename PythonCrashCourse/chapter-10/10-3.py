file_name = 'guest.txt'
name = input('Please input your name:')
with open(file_name,'w') as f_obj:
    f_obj.write(name)
