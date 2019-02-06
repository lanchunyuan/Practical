# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# pprint.pprint(count)

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# b = []
# eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
# for i in eggs.items():
#     print(i)
#     a = list(i)
#     print(a)
#     b = a + b
# print(b)

# picnicItems = {'apples': 5, 'cups': 2}
#
# message = 'I am bringing ' + str(picnicItems.get('apples',0)) + ' apples.'
#
# print(message)
#
# message = 'I am bringing ' + str(picnicItems.get('pairs',0)) + ' pairs.'
#
# print(message)


"""
# find how manay time the item appears in the list??????
"""

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         print(value + ' : ' + str(some_list.count(value)) )
# #         if value not in duplicates:
# #             duplicates.append(value)
# #
# # print(duplicates)

"""查找 list中重复的值"""

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# duplicattes = set([x for x in some_list if some_list.count(x) > 1 ])
#
# print(duplicattes)


# a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
# b = set(a)
# # print(b)
# for each_b in b:
#     count = 0
#     for each_a in a:
#         if each_b == each_a:
#             count += 1
#     print(each_b, ": ", count)


# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# quoto = ['I','am','lucky','!']
# # message = ' '.join(quoto)
# # print(message)
# #
# # split_list = message.split(' ')
# # print(split_list)

# import pyperclip

# pyperclip.copy('Hello world!')
# print(pyperclip.paste())

# text = pyperclip.paste()
# print(text)
# lines = text.split('\r\n')
# # for line in lines:
# #     print(f'* {line}')
# print()
#
# for i in range(len(lines)):
#     lines[i] = '*' + lines[i]
# text = '\n'.join(lines)
# print(text)
# pyperclip.copy(text)

import re

# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# heroRegex = re.compile(r'Batman|Tina Fey')
# m1 = heroRegex.search('Batman and Tina Fey')
# print(m1.group())

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# message = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
# Eve knew Agent Bob was a double agent.')
# print(message)

# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))? # area code
# (\s|-|\.)? # separator
# \d{3} # first 3 digits
# (\s|-|\.) # separator
# \d{4} # last 4 digits
# (\s*(ext|x|ext.)\s*\d{2,5})? # extension
# )''', re.VERBOSE)

