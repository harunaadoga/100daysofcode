#! /usr/bin/env python3
#A password store for commonly used accounts
import pyperclip
import sys

# store passwords
passes = {'Google':'go21233', 'Ebay':'ba23443@', 'Udemy':'Dem123£@@',
'Yahoo':'iei30201', 'Netflix':'iri(@*£'}
#check and copy password
if len(sys.argv) < 2:
    print('Enter an account to copy password')
    sys.exit()
account = sys.argv[1] #the first argument passed
if account in passes:
    pyperclip.copy(passes[account])
    print('The password for '+account+' has been copied successfully')
else:
    print(account + 'account not in password store')


