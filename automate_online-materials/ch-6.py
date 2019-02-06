tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
str_len = []
for item in tableData:
    for i in item:
        str_len.append(len(i))
width = max(str_len)
# print(width)

def printTable(spam):
    for i in range(len(spam[0])):
        for j in range(len(spam)):
            if j == 0:
                print(spam[j][i].rjust(width),end=' ')
            else:
                print(spam[j][i].ljust(width), end='')
        print()

printTable(tableData)