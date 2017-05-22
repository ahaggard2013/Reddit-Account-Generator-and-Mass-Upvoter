#!/usr/bin/env python
import random
import string


def generate_username_password(amount, ulength, plength, list):
    for _ in range(0,amount):
        list.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(ulength)) + ':'+ ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(plength)) + '\n')

        
list = open('redditNameList.txt', 'w')
generate_username_password(100,15,15, list)
list.close()
