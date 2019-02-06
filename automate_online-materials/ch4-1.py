spam = ['apples', 'bananas', 'tofu', 'cats']
def print_list(spam):
    for i in range(0,len(spam)):
        if i != len(spam) - 1:
            print(spam[i],end=',')
        else:
            print('and ' + spam[i])

print_list(spam)
# print(spam[0])
# for i in range(4):
#     print(spam[i],end=',')