# assert(spam >= 10, 'The spam variable is less than 10.')

# def num(spam):
#     assert spam >=10,"The spam variable is less than 10"
#     print(spam)
#
# num(11)
# num(6)

# def str_compar(eggs,bacon):
#     assert eggs.lower() == bacon.lower(),"The strings are not the same!"
#     print("The strings are same!")
# str_A = input("input string A:")
# str_B = input("Enter string B:")
# str_compar(str_A,str_B)



#
# import logging
#
# logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#
# logging.basicConfig(filename='loging.txt',level=logging.INFO,format='%(asctime)s  %(levelnome)s  %(message)s')
#
# DEBUG INFO WARING ERROR CRITICAL
#
# logging.disable(logging.CRITICAL)

# import random,logging
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s  %(levelname)s  %(message)s')
# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input()
# # toss = random.randint('0', '1') # 0 is tails, 1 is heads
# toss = random.choice(['heads', 'tails'])
# logging.debug(f'toss is {toss},and guess is {guess}')
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')


# import logging
# logging.basicConfig(                             level=logging.INFO, format='%(asctime)s, %(levelname)s - %(message)s')
# #logging.basicConfig(filename='myProgramLog.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# import random
#
# def guess_fun():
#     global guess
#     while guess not in ('heads', 'tails'):
#         print('Guess the coin toss! Enter heads or tails:')
#         guess = input()
#
# guess = ''
# guess_fun()
# toss = random.choice(['heads', 'tails']) # 0 is tails, 1 is heads
# logging.info('toss is %s, guess is %s' % (toss, guess))
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = ''
#     guess_fun()
#     logging.info('toss is %s, guess is %s' % (toss, guess))
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')

import webbrowser,requests,pyperclip

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)
print(res.text[:1000])
with open('a.txt','a',encoding='utf-8') as f_obj:
    f_obj.write(res.text)
# webbrowser.open('www.baidu.com')