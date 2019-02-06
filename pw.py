# a password dict
PASSWORDS = \
{
    'test':     '4KtU8DR355Hb',
    'dev':      'xHQTvokdlGRh',
    'switch':   'Tnl47Z5fXsUv',
    'email':    'Lancy@82'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
