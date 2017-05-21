#!/usr/bin/env python
import random
import string

list = open('redditNameList.txt', 'w')

def generate_username_password(amount, ulength, plength):
    for _ in range(0,amount):
        list.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(ulength)) + ':'+ ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(plength)) + '\n')

        
generate_username_password(100,15,15)
list.close()
